import sys
import numpy as np
import pandas as pd
import tensorflow as tf
import pennylane as qml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler
from sklearn.decomposition import PCA
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from ui_form import Ui_Widget
from itertools import combinations
from scipy.stats import zscore
from sklearn.preprocessing import LabelEncoder
from qiskit_ibm_provider import IBMProvider
import qnnlib


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Initialize variables
        self.csv_file = ""
        self.backend = ""
        self.number_of_qubits = 0
        self.reps = 0
        self.dev = ""

        # Connect UI elements to methods
        self.ui.pushButton.clicked.connect(self.open_file_picker)
        self.ui.pushButton_2.clicked.connect(self.start_training)
        self.ui.comboBox.currentTextChanged.connect(self.update_backend)

        # Connect the QTextEdit elements from the UI file
        # Initialize your inputs here if needed
        self.NumOQubEdit = self.ui.NumOQubEdit
        self.EpochsEdit = self.ui.EpochsEdit
        self.TrainSplitEdit = self.ui.TrainSplitEdit
        self.BatchEdit = self.ui.BatchEdit
        self.RepsEdit = self.ui.RepsEdit
        self.ExportNameEdit = self.ui.ExportNameEdit

    def open_file_picker(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_name:
            self.csv_file = file_name
            self.update_selected_file_label()

    def update_selected_file_label(self):
        self.ui.label_2.setText(f'Selected file: {self.csv_file}')

    def update_backend(self, text):
        if text == "Select a backend":
            self.backend = None
        else:
            self.backend = text
        print(f'Backend selected: {self.backend}')

    def ZZFeatureMap(self, nqubits, data):
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

    def TwoLocal(self, nqubits, theta, reps):
        for r in range(reps):
            for i in range(nqubits):
                qml.RY(theta[r * nqubits + i], wires=i)
            for i in range(nqubits - 1):
                qml.CNOT(wires=[i, i + 1])
        for i in range(nqubits):
            qml.RY(theta[reps * nqubits + i], wires=i)

    def qnn_circuit(self, inputs, theta):
        self.ZZFeatureMap(self.number_of_qubits, inputs)
        self.TwoLocal(nqubits=self.number_of_qubits, theta=theta, reps=self.reps)
        return qml.expval(qml.Hermitian(self.M_global, wires=[0]))
    

    def start_training(self):
        print("Traning start...")
        if not self.csv_file:
            QMessageBox.warning(self, "Warning", "Please select a CSV file before starting the training.")
            return

        try:
            epochs = int(self.EpochsEdit.text())  # ใช้ EpochsEdit
            train_test_split_ratio = int(self.TrainSplitEdit.text())
            batch_size = int(self.BatchEdit.text())
            self.reps = int(self.RepsEdit.text())
            self.number_of_qubits = int(self.NumOQubEdit.text())

            if train_test_split_ratio < 0 or train_test_split_ratio > 100:
                raise ValueError("Train/Test split ratio must be between 0 and 100.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numerical values.")
            return
        # Set up the experiment with qnnlib
        self.run_qnnlib_experiment(
            data_path=self.csv_file,
            #target_column='RiskLevel',  # Assuming "Outcome" is the target column in your dataset
            test_size=train_test_split_ratio / 100,
            batch_size=batch_size,
            epochs=epochs,
            reps=self.reps
        )

    def run_qnnlib_experiment(self, data_path, test_size, batch_size, epochs, reps):
        df = pd.read_csv(data_path)
        print(f"จำนวนข้อมูลก่อนการทำ Data Cleansing: {df.shape}")
        # ตรวจหาและจัดการ Missing Values
        for column in df.columns:
            if df[column].isnull().any():
                if df[column].dtype in ['float64', 'int64']:
                    print(f"เติมค่าเฉลี่ยในคอลัมน์: {column}")
                    df[column].fillna(df[column].mean(), inplace=True)
                else:
                    print(f"เติมค่าที่พบบ่อยที่สุดในคอลัมน์: {column}")
                    df[column].fillna(df[column].mode()[0], inplace=True)
        # แปลง Categorical Features เป็นตัวเลข
        label_encoders = {}  # เก็บ LabelEncoders สำหรับการแปลงกลับ (ถ้าจำเป็น)
        for column in df.select_dtypes(include=['object']).columns:
            print(f"แปลงข้อมูล Categorical ในคอลัมน์: {column}")
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            label_encoders[column] = le  # เก็บ encoder สำหรับ reference

        # กำจัด Outliers โดยใช้ Z-score (หากค่าเกิน 3 หรือ -3 ถือว่าเป็น Outlier)
        df = df[(np.abs(zscore(df.select_dtypes(include=[np.number]))) < 3).all(axis=1)]
        print(f"จำนวนข้อมูลหลังการทำ Data Cleansing: {df.shape}")
        
        clean_data_path = "cleaned_data.csv"
        df.to_csv(clean_data_path, index=False)

        print(f"Cleaned data saved to: {clean_data_path}")
        target_column = df.columns[-1]


        qnn = qnnlib.qnnlib(nqubits=self.number_of_qubits, device_name=self.backend)

        # Set the output paths for model and progress
        model_output_path = self.ExportNameEdit.text()
        if not model_output_path.endswith(".h5"):
            model_output_path += ".h5"
        csv_output_path = 'training_progress.csv'
        loss_plot_file = 'loss_plot.png'
        accuracy_plot_file = 'accuracy_plot.png'
        print(f'Data path: {data_path}')
        print(f'Taget column: {target_column}')
        print(f'Test size: {test_size}')
        print(f'Batch size: {batch_size}')
        print(f'Epochs: {epochs}')
        print(f'Reps: {reps}')

        # Run the experiment using qnnlib
        qnn.run_experiment(
            data_path=clean_data_path,
            target=target_column,
            test_size=test_size,
            model_output_path=model_output_path,
            csv_output_path=csv_output_path,
            loss_plot_file=loss_plot_file,
            accuracy_plot_file=accuracy_plot_file,
            batch_size=batch_size,
            epochs=epochs,
            reps=reps,
            optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.001),
            seed=1234
        )
        QMessageBox.information(self, "Training Complete", f"The model has been trained and saved as {model_output_path}.")

    def plot_losses(self, history):
        import matplotlib.pyplot as plt
        tr_loss = history.history["loss"]
        val_loss = history.history["val_loss"]
        epochs = range(1, len(tr_loss) + 1)

        plt.figure()
        plt.plot(epochs, tr_loss, 'b', label='Training loss')
        plt.plot(epochs, val_loss, 'r', label='Validation loss')
        plt.title('Training and Validation Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Widget()
    main_window.show()
    sys.exit(app.exec())
