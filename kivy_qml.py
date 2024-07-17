from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang.builder import Builder

# Define the .kv layout directly in the Python script for simplicity
kv = """
<SetOptimize>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Model Accuracy Details'
            color: 0, 0, 0, 1
            font_size: 18
            size_hint_y: None
            height: 40
        Label:
            text: 'Accuracy: 95%'
            color: 0, 0, 0, 1
        Label:
            text: 'Loss: 0.05'
            color: 0, 0, 0, 1
        Label:
            text: 'Precision: 92%'
            color: 0, 0, 0, 1
        Label:
            text: 'Recall: 93%'
            color: 0, 0, 0, 1
    GridLayout:
        cols: 2
        size_hint_y: None
        height: 100
        Label:
            text: 'Epoch:'
            color: 0, 0, 0, 1  # Set font color to black
        TextInput:
            id: epoch
            multiline: False
        Label:
            text: 'Learning Rate:'
            color: 0, 0, 0, 1  # Set font color to black
        TextInput:
            id: learning_rate
            multiline: False
        Label:
            text: 'Batch Size:'
            color: 0, 0, 0, 1  # Set font color to black
        TextInput:
            id: batch_size
            multiline: False

<FileInput>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    FileChooserListView:
        id: filechooser
    Button:
        text: 'Upload File'
        size_hint_y: None
        height: 50
        on_release: root.upload_file(self)

<OutputDisplay>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    Label:
        id: output_label
        text: 'Output will be displayed here.'
        color: 0, 0, 0, 1  # Set font color to black

<MainLayout>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    SetOptimize:
        id: set_optimize
        size_hint_y: None
        height: 350
    FileInput:
        id: file_input
        size_hint_y: None
        height: 300
    OutputDisplay:
        id: output_display
        size_hint_y: None
        height: 100
    Button:
        text: 'Start Optimization'
        size_hint_y: None
        height: 50
        on_release: app.start_optimization()
"""

Builder.load_string(kv)

class SetOptimize(BoxLayout):
    pass

class FileInput(BoxLayout):
    def upload_file(self, instance):
        selected = self.ids.filechooser.selection
        if selected:
            file_path = selected[0]
            print(f'File selected: {file_path}')
            popup = Popup(title='File Uploaded',
                          content=Label(text=f'File {file_path} selected!'),
                          size_hint=(0.6, 0.4))
            popup.open()

class OutputDisplay(BoxLayout):
    def update_output(self, loss, accuracy):
        self.ids.output_label.text = f'Loss: {loss}\nAccuracy: {accuracy}' 

class MainLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.8, 0.8, 0.8, 1)
        return MainLayout()

    def start_optimization(self):
        # Example function to simulate optimization process
        loss = 0.05  # Example loss value
        accuracy = 95  # Example accuracy value
        self.root.ids.output_display.update_output(loss, accuracy)

if __name__ == '__main__':
    MyApp().run()
