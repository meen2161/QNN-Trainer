import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

"""--------------------------------------------
Load ML Library to using a train and a test set
--------------------------------------------"""
import pennylane as qml
import numpy as np
import tensorflow as tf
import keras

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd

from qiskit_ibm_provider import IBMProvider
IBMProvider.save_account("c6114a56ebddc3cdae7337953a114c0d8bca94aa0e079ee893a7415b102dc3aab8b46db8306bd72726b9af72f42cad98f789cb15adcf1a466a99f0b79c124a43", overwrite="True")


from sklearn.decomposition import PCA
from itertools import combinations


class FilePickerPopup(Popup):
    def __init__(self, **kwargs):
        super(FilePickerPopup, self).__init__(**kwargs)
        self.title = 'Pick a CSV file'
        self.size_hint = (0.9, 0.9)
        self.filechooser = FileChooserIconView(filters=['*.csv'], path=os.getcwd())
        self.filechooser.bind(on_submit=self.file_selected)
        self.add_widget(self.filechooser)

    def file_selected(self, filechooser, selection, touch):
        if selection:
            self.parent_widget.csv_file = selection[0]
            self.parent_widget.update_selected_file_label()
            print(f'Selected file: {self.parent_widget.csv_file}')
            self.dismiss()

class QuantumMLApp(BoxLayout):
    csv_file = StringProperty('')
    backend = StringProperty('Simulator')
    epochs = StringProperty('')
    train_test_split = StringProperty('')
    batch_size = StringProperty('')
    current_epoch = StringProperty('')
    M_global = 0
    #dev = None


    number_of_qubits = 4

    dev = qml.device("default.qubit", wires=number_of_qubits)

    def ZZFeatureMap(self,nqubits, data):
        nload = min(len(data), nqubits)
        for i in range(nload):
            qml.Hadamard(i)
            qml.RZ(2.0 * data[:, i], wires=i)
        for pair in list(combinations(range(nload), 2)):
            q0 = pair[0]
            q1 = pair[1]
            qml.CZ(wires=[q0, q1])
            qml.RZ(2.0 * (np.pi - data[:, q0]) * (np.pi - data[:, q1]), wires=q1)
            qml.CZ(wires=[q0, q1])

    def TwoLocal(self, nqubits, theta, reps=1):
        for r in range(reps):
            for i in range(nqubits):
                qml.RY(theta[r * nqubits + i], wires=i)
            for i in range(nqubits - 1):
                qml.CNOT(wires=[i, i + 1])
        for i in range(nqubits):
            qml.RY(theta[reps * nqubits + i], wires=i)

    def qnn_circuit(self, inputs, theta):
        self.ZZFeatureMap(self.number_of_qubits, inputs)
        self.TwoLocal(nqubits=self.number_of_qubits, theta=theta, reps=1)
        return qml.expval(qml.Hermitian(self.M_global, wires=[0]))
    

    def set_qubit_size(self, qbit):
        number_of_qubits = qbit
    

    def __init__(self, **kwargs):
        super(QuantumMLApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.selected_file_label = Label(text='',size_hint=(None,None),size=(500,200),pos_hint= {'center_x': 0.4,'center_y': 0.5})
        
        # Create a horizontal BoxLayout for the file picker button and label
        file_picker_layout = BoxLayout(orientation='horizontal')
        # Selected file label
        self.selected_file_label = Label(text='No file selected', size_hint=(None, None), size=(1000, 100), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        file_picker_layout.add_widget(self.selected_file_label)

        # File picker button
        file_picker_button = Button(text='Select CSV File',size_hint=(None, None), size=(500, 100), pos_hint={'center_x': 0.7, 'center_y': 0.5})
        file_picker_button.bind(on_press=self.open_file_picker)
        file_picker_layout.add_widget(file_picker_button)
        


        # Add the horizontal BoxLayout to the main layout
        self.add_widget(file_picker_layout)

        # Backend selection
        backend_spinner = Spinner(
            text='Simulator',
            values=('Simulator', 'Real Quantum Machine'),
            size_hint=(None, None),
            size=(400, 44),
            pos_hint={'center_x': 0.5,'center_y': 100}
        )
        backend_spinner.bind(text=self.update_backend)
        self.add_widget(backend_spinner)

        # Configuration inputs
        config_layout = BoxLayout(orientation='vertical')
        # Epochs input
        config_layout.add_widget(Label(text='Epochs:', size_hint=(None, None), size=(100, 44),pos_hint = {'center_x': 0.2,'center_y': 0.0}))
        self.epochs_input = TextInput(multiline=False, size_hint=(None, None), size=(100, 44),pos_hint = {'center_x': 0.2,'center_y': 0.0})
        config_layout.add_widget(self.epochs_input)

        # Train/Test split input
        config_layout.add_widget(Label(text='Train/Test Split (%):', size_hint=(None, None), size=(100, 44),pos_hint = {'center_x': 0.2,'center_y': 0.0}))
        self.split_input = TextInput(multiline=False, size_hint=(None, None), size=(100, 44),pos_hint = {'center_x': 0.2,'center_y': 0.0})
        config_layout.add_widget(self.split_input)

        # Batch size input
        config_layout.add_widget(Label(text='Batch Size:', size_hint=(None, None), size=(100, 44),pos_hint = {'center_x': 0.2,'center_y': 0.0}))
        self.batch_input = TextInput(multiline=False, size_hint=(None, None), size=(100, 44),pos_hint = {'center_x': 0.2,'center_y': 0.0})
        config_layout.add_widget(self.batch_input)

        self.add_widget(config_layout)

        # Status bar
        self.status_bar = Label(text='Current Epoch: 0')
        self.add_widget(self.status_bar)

        # Start button
        start_button = Button(text='Start Training',size_hint=(None,None),size=(400,100),pos_hint= {'center_x': 0.5,'center_y': 0.5})
        start_button.bind(on_press=self.start_training)
        self.add_widget(start_button)
        self.add_widget(Widget(size_hint_y=None, height=100))




    def open_file_picker(self, instance):
        file_picker_popup = FilePickerPopup()
        file_picker_popup.parent_widget = self
        file_picker_popup.open()

    def update_selected_file_label(self):
        self.selected_file_label.text = f'Selected file: {self.csv_file}'

    def update_backend(self, spinner, text):
        self.backend = text
        if self.backend == 'Simulator':
            self.dev = qml.device("default.qubit", wires=self.number_of_qubits)
        
        else:
            self.dev = qml.device('qiskit.ibmq', wires=self.number_of_qubits, backend='ibm_kyoto')



        print(f'Backend selected: {self.backend}')



    def start_training(self, instance):
        self.epochs = self.epochs_input.text
        self.train_test_split = self.split_input.text
        self.batch_size = self.batch_input.text
        self.current_epoch = self.epochs  # Just an example, should be updated during training
        self.status_bar.text = f'Current Epoch: {self.current_epoch}'
        df = pd.read_csv(self.csv_file)

        x = df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
        y= df['Outcome']

        x_tr, x_test, y_tr, y_test = train_test_split(
            x, y, train_size = int(self.train_test_split))
        x_val, x_test, y_val, y_test = train_test_split(
            x_test, y_test, train_size = 0.5)


        seed = 4321
        np.random.seed(seed)
        tf.random.set_seed(seed)

        scaler = MaxAbsScaler()
        x_tr = scaler.fit_transform(x_tr)
        x_test = scaler.transform(x_test)
        x_val = scaler.transform(x_val)

        x_test = np.clip(x_test, 0, 1)
        x_val = np.clip(x_val, 0, 1)


        pca = PCA(n_components = 4)
        xs_tr = pca.fit_transform(x_tr)
        xs_test = pca.transform(x_test)
        xs_val = pca.transform(x_val)

        state_0 = [[1], [0]]
        print(state_0 * np.conj(state_0).T)
        self.M_global = state_0 * np.conj(state_0).T

        #dev = qml.device("default.qubit", wires=self.number_of_qubits)
        qnn = qml.QNode(self.qnn_circuit, self.dev, interface="tf")



        weights = {"theta": 8}
        qlayer = qml.qnn.KerasLayer(qnn, weights, output_dim=1)

        model = tf.keras.models.Sequential([qlayer])


        opt = tf.keras.optimizers.Adam(learning_rate = 0.005)
        model.compile(opt, loss=tf.keras.losses.BinaryCrossentropy(),  metrics=[keras.metrics.BinaryAccuracy()])


        earlystop = tf.keras.callbacks.EarlyStopping(
            monitor = "val_loss", patience = 2, verbose = 1,
            restore_best_weights = True)

        print (xs_tr.shape)
        print (y_tr.shape)
        print(self.epochs)
        history = model.fit(xs_tr, y_tr, epochs = int(self.epochs), shuffle = True,
            validation_data = (xs_val, y_val),
            batch_size = int(self.batch_size), 
            callbacks = [earlystop])



        print(f'Starting training with {self.epochs} epochs, {self.train_test_split}% train/test split, batch size {self.batch_size}, on {self.backend} backend.')

    def print_choices(self, instance):
        print(f'Selected file: {self.csv_file}')
        print(f'Backend: {self.backend}')
        print(f'Epochs: {self.epochs_input.text}')
        print(f'Train/Test Split: {self.split_input.text}')
        print(f'Batch Size: {self.batch_input.text}')

class QuantumMLAppMain(App):
    def build(self):
        return QuantumMLApp()

if __name__ == '__main__':
    QuantumMLAppMain().run()
