# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
#     QSizePolicy, QTextEdit, QWidget, QVBoxLayout)

# class Ui_Widget(object):
#     def setupUi(self, Widget):
#         if not Widget.objectName():
#             Widget.setObjectName(u"Widget")
#         Widget.resize(1169, 640)

#         # Layout สำหรับให้ widget เรียงตามแนวตั้ง
#         layout = QVBoxLayout(Widget)
        
#         self.label = QLabel(Widget)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(500, 20, 191, 51))
#         font = QFont()
#         font.setPointSize(25)
#         self.label.setFont(font)
#         self.label_2 = QLabel(Widget)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(480, 120, 481, 21))
#         font1 = QFont()
#         font1.setPointSize(10)
#         self.label_2.setFont(font1)
#         self.pushButton = QPushButton(Widget)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(220, 110, 191, 41))
#         font2 = QFont()
#         font2.setPointSize(15)
#         self.pushButton.setFont(font2)
#         self.pushButton_2 = QPushButton(Widget)
#         self.pushButton_2.setObjectName(u"pushButton_2")
#         self.pushButton_2.setGeometry(QRect(490, 520, 211, 61))
#         self.pushButton_2.setFont(font2)
#         self.comboBox = QComboBox(Widget)
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.setObjectName(u"comboBox")
#         self.comboBox.setGeometry(QRect(220, 160, 191, 31))
#         self.label_3 = QLabel(Widget)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setGeometry(QRect(248, 290, 61, 20))
#         font3 = QFont()
#         font3.setPointSize(12)
#         self.label_3.setFont(font3)
#         self.ApiInput = QTextEdit(Widget)
#         self.ApiInput.setObjectName(u"ApiInput")
#         self.ApiInput.setGeometry(QRect(320, 280, 581, 31))
#         self.label_4 = QLabel(Widget)
#         self.label_4.setObjectName(u"label_4")
#         self.label_4.setGeometry(QRect(320, 470, 51, 20))
#         self.label_4.setFont(font3)
#         self.label_5 = QLabel(Widget)
#         self.label_5.setObjectName(u"label_5")
#         self.label_5.setGeometry(QRect(600, 350, 141, 20))
#         self.label_5.setFont(font3)
#         self.label_6 = QLabel(Widget)
#         self.label_6.setObjectName(u"label_6")
#         self.label_6.setGeometry(QRect(660, 410, 81, 20))
#         self.label_6.setFont(font3)
#         self.EpochsInput = QTextEdit(Widget)
#         self.EpochsInput.setObjectName(u"EpochsInput")
#         self.EpochsInput.setGeometry(QRect(380, 460, 81, 31))
#         self.TrainSplitInput = QTextEdit(Widget)
#         self.TrainSplitInput.setObjectName(u"TrainSplitInput")
#         self.TrainSplitInput.setGeometry(QRect(750, 340, 81, 31))
#         self.BatchInput = QTextEdit(Widget)
#         self.BatchInput.setObjectName(u"BatchInput")
#         self.BatchInput.setGeometry(QRect(750, 400, 81, 31))
#         self.label_7 = QLabel(Widget)
#         self.label_7.setObjectName(u"label_7")
#         self.label_7.setGeometry(QRect(550, 470, 181, 20))
#         self.label_7.setFont(font3)
#         self.ExportNameInput = QTextEdit(Widget)
#         self.ExportNameInput.setObjectName(u"ExportNameInput")
#         self.ExportNameInput.setGeometry(QRect(750, 460, 151, 31))
#         self.label_8 = QLabel(Widget)
#         self.label_8.setObjectName(u"label_8")
#         self.label_8.setGeometry(QRect(240, 350, 131, 20))
#         self.label_8.setFont(font3)
#         self.NumOQubInput = QTextEdit(Widget)
#         self.NumOQubInput.setObjectName(u"NumOQubInput")
#         self.NumOQubInput.setGeometry(QRect(380, 340, 81, 31))
#         self.RepsInput = QTextEdit(Widget)
#         self.RepsInput.setObjectName(u"RepsInput")
#         self.RepsInput.setGeometry(QRect(380, 400, 81, 31))
#         self.RepsInput.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
#         self.label_9 = QLabel(Widget)
#         self.label_9.setObjectName(u"label_9")
#         self.label_9.setGeometry(QRect(330, 410, 41, 20))
#         self.label_9.setFont(font3)

        
#         # ส่วนของแสดง UI Terminal
#         self.terminal_output = QTextEdit(Widget)
#         self.terminal_output.setReadOnly(True)  # ไม่ให้แก้ไขได้
#         layout.addWidget(self.terminal_output)

#         self.retranslateUi(Widget)

#         QMetaObject.connectSlotsByName(Widget)
#     # setupUi

#     def retranslateUi(self, Widget):
#         Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
#         self.label.setText(QCoreApplication.translate("Widget", u"QNN Trainer", None))
#         self.label_2.setText(QCoreApplication.translate("Widget", u"No file selected", None))
#         self.pushButton.setText(QCoreApplication.translate("Widget", u"Select file", None))
#         self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Start Training", None))
#         self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Select a backend", None))
#         self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"default.qubit", None))
#         self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"Real Quantum Machine", None))
#         self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"lightning.qubit", None))
#         self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"qiskit.aer", None))

#         self.label_3.setText(QCoreApplication.translate("Widget", u"Api Key:", None))
#         self.label_4.setText(QCoreApplication.translate("Widget", u"Epochs:", None))
#         self.label_5.setText(QCoreApplication.translate("Widget", u"Train/Test Split (%):", None))
#         self.label_6.setText(QCoreApplication.translate("Widget", u"Batch Size:", None))
#         self.label_7.setText(QCoreApplication.translate("Widget", u"Exported model file name:", None))
#         self.label_8.setText(QCoreApplication.translate("Widget", u"Number of qubits:", None))
#         self.RepsInput.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#         self.label_9.setText(QCoreApplication.translate("Widget", u"Reps:", None))
#     # retranslateUi

# import sys
# from PySide6.QtCore import QCoreApplication, QMetaObject, QTimer, Qt, QRect
# from PySide6.QtGui import QFont, QTextCursor
# from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, 
#                                QTextEdit, QWidget, QHBoxLayout, QVBoxLayout, 
#                                QFrame, QComboBox, QGridLayout, QLineEdit, QSizePolicy, QSpacerItem)

# class Ui_Widget(object):
#     def setupUi(self, Widget):
#         Widget.setObjectName(u"Widget")
#         Widget.resize(1200, 640)
#         #self.mainLayout = QHBoxLayout(Widget)
#         self.gridLayout = QGridLayout(Widget)

#         # ================== ส่วนกรอกข้อมูลด้านซ้าย ==================
#         self.topLayout = QVBoxLayout()

#         self.label = QLabel("QNN Trainer")
#         self.label.setFont(QFont("", 25))
#         self.label.setAlignment(Qt.AlignCenter)
#         self.topLayout.addWidget(self.label)

#         self.fileLayout = QHBoxLayout()
#         self.pushButton = QPushButton("Select File")
#         self.pushButton.setFixedWidth(200)
#         self.pushButton.setFont(QFont("", 15))
#         self.fileLayout.addWidget(self.pushButton, alignment=Qt.AlignCenter)
        
#         self.label_2 = QLabel("No file selected")
#         self.fileLayout.addWidget(self.label_2)
#         self.topLayout.addLayout(self.fileLayout)
#         self.topLayout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

#         self.comboAndApiLayout = QHBoxLayout()


#         self.comboBox = QComboBox()
#         self.comboBox.addItems([
#             "Select a backend", "default.qubit", 
#             "Real Quantum Machine", "lightning.qubit", "qiskit.aer"
#         ])
#         self.comboBox.setFont(QFont("", 12))
#         self.comboBox.setMinimumHeight(25)
#         self.comboAndApiLayout.addWidget(self.comboBox)

#         # Inputs Section

#         self.apiLabel = QLabel("API Key:")
#         self.apiLabel.setFont(QFont("", 12))
#         self.comboAndApiLayout.addWidget(self.apiLabel)

#         self.apiInput = QLineEdit()
#         self.apiInput.setFont(QFont("", 12))
#         self.apiInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.comboAndApiLayout.addWidget(self.apiInput)
        
#         self.topLayout.addLayout(self.comboAndApiLayout)
        
#         self.gridLayout.addLayout(self.topLayout, 0, 0, 1, 2)
#         self.topLayout.addItem(QSpacerItem(10, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
#         self.bottomLeftLayout = QVBoxLayout()
#         self.gridLayout.addLayout(self.bottomLeftLayout, 1, 0)
        
#         self.NumOQubInput = QTextEdit()
#         self.NumOQubInput.setObjectName("NumOQubInput")
#         self.EpochsInput.setFixedHeight(40)  # ตั้งความสูงของ QTextEdit
#         self.EpochsInput.setFixedWidth(200)   # ตั้งความกว้างของ QTextEdit
#         self.EpochsInput = QTextEdit()  # เปลี่ยนเป็น QTextEdit
#         self.EpochsInput.setObjectName("EpochsInput")
#         self.EpochsInput.setFixedHeight(40)  # ตั้งความสูงของ QTextEdit
#         self.EpochsInput.setFixedWidth(200)   # ตั้งความกว้างของ QTextEdit
#         # เปลี่ยน input sections เป็น QTextEdit
#         self.TrainSplitInput = QTextEdit()  # เปลี่ยนเป็น QTextEdit
#         self.TrainSplitInput.setObjectName("TrainSplitInput")
#         self.TrainSplitInput.setFixedHeight(40)
#         self.TrainSplitInput.setFixedWidth(200)

#         self.BatchInput = QTextEdit()  # เปลี่ยนเป็น QTextEdit
#         self.BatchInput.setObjectName("BatchInput")
#         self.BatchInput.setFixedHeight(40)
#         self.BatchInput.setFixedWidth(200)

#         self.RepsInput = QTextEdit()  # เปลี่ยนเป็น QTextEdit
#         self.RepsInput.setObjectName("RepsInput")
#         self.RepsInput.setFixedHeight(40)
#         self.RepsInput.setFixedWidth(200)

#         self.ExportNameInput = QTextEdit()  # เปลี่ยนเป็น QTextEdit
#         self.ExportNameInput.setObjectName("ExportNameInput")
#         self.ExportNameInput.setFixedHeight(40)
#         self.ExportNameInput.setFixedWidth(200)

#         # เพิ่ม QTextEdit ลงใน layout
#         self.bottomLeftLayout.addWidget(self.NumOQubInput)
#         self.bottomLeftLayout.addWidget(self.EpochsInput)
#         self.bottomLeftLayout.addWidget(self.TrainSplitInput)
#         self.bottomLeftLayout.addWidget(self.BatchInput)
#         self.bottomLeftLayout.addWidget(self.RepsInput)
#         self.bottomLeftLayout.addWidget(self.ExportNameInput)
        
# #         self.bottomLeftLayout = QVBoxLayout()
# #         self.gridLayout.addLayout(self.bottomLeftLayout, 1, 0)
# #         self.NumOQubInput = self.create_input_section("Number of Qubits:")
# #         self.EpochsInput = QLineEdit(Widget)
# #         self.EpochsInput.setObjectName("EpochsInput")
# #         self.EpochsInput.setGeometry(QtCore.QRect(100, 100, 200, 40))
# # #         self.TrainSplitInput = QTextEdit(Widget)
# # #         self.TrainSplitInput.setObjectName(u"TrainSplitInput")
# # #         self.TrainSplitInput.setGeometry(QRect(750, 340, 81, 31))
# # #         self.BatchInput = QTextEdit(Widget)
# # #         self.BatchInput.setObjectName(u"BatchInput")
# # #         self.BatchInput.setGeometry(QRect(750, 400, 81, 31))
# #         self.RepsInput = self.create_input_section("Reps:")
# #         self.TrainSplitInput = self.create_input_section("Train/Test Split (%):")
# #         self.BatchInput = self.create_input_section("Batch Size:")
# #         self.ExportNameInput = self.create_input_section("Exported Model File Name:")
        
#         for widget in [self.NumOQubInput, self.EpochsInput, self.RepsInput, 
#             self.TrainSplitInput, self.BatchInput, self.ExportNameInput]:
#             self.bottomLeftLayout.addWidget(widget)

#         self.pushButton_2 = QPushButton("Start Training")
#         self.pushButton_2.setFont(QFont("", 15))
#         self.pushButton_2.setFixedWidth(200)
#         self.pushButton_2.clicked.connect(self.start_training)  # ผูกปุ่มกับฟังก์ชัน start_training
#         self.bottomLeftLayout.addWidget(self.pushButton_2, alignment=Qt.AlignCenter)


#         # ================== ส่วน Terminal Output ด้านขวา ==================
#         self.bottomRightLayout = QVBoxLayout()
#         # self.terminalLabel = QLabel("Terminal:")
#         # self.terminalLabel.setFont(QFont("", 12))
#         # self.bottomRightLayout.addWidget(self.terminalLabel)

#         self.terminalOutput = QTextEdit()
#         self.terminalOutput.setReadOnly(True)
#         self.terminalOutput.setMinimumSize(400, 300)  # กำหนดขนาดเริ่มต้น
#         self.terminalOutput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.bottomRightLayout.addWidget(self.terminalOutput)

#         # เพิ่ม Layout Terminal ด้านขวา และขยายให้ครอบหลายคอลัมน์หรือแถว
#         self.gridLayout.addLayout(self.bottomRightLayout, 1, 1, 2, 2)  # ขยายครอบ 2x2 (rowSpan, columnSpan)

#         # กำหนดสัดส่วนของคอลัมน์และแถวใหม่
#         self.gridLayout.setColumnStretch(0, 1)  # พื้นที่ด้านซ้าย (ข้อมูล)
#         self.gridLayout.setColumnStretch(1, 3)  # พื้นที่ด้านขวา (Terminal)

#         self.gridLayout.setRowStretch(0, 1)  # แถวบน (ชื่อเรื่องและปุ่มไฟล์)
#         self.gridLayout.setRowStretch(1, 4)  # แถวกลาง (ข้อมูล)
#         #self.gridLayout.setRowStretch(3, 5)  # แถวล่าง (Terminal ขยายใหญ่ขึ้น)

#         # Redirect stdout ไปที่ QTextEdit
#         sys.stdout = CustomStream(self.terminalOutput)

#         self.retranslateUi(Widget)
#         QMetaObject.connectSlotsByName(Widget)

#     def create_input_section(self, label_text):
#         input_widget = QWidget()
#         layout = QHBoxLayout(input_widget)

#         # สร้าง QLabel และจัดให้ชิดขวา
#         label = QLabel(label_text)
#         label.setFont(QFont("", 12))
#         label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # ชิดขวาและจัดให้อยู่กึ่งกลางแนวตั้ง
#         label.setFixedWidth(250)
#         layout.addWidget(label)

#         # สร้าง QLineEdit สำหรับรับค่า
#         textEdit = QTextEdit()
#         textEdit.setFixedHeight(30)
#         textEdit.setFixedWidth(200)  # ความกว้างของช่องรับค่า
#         layout.addWidget(textEdit)

#         # ป้องกันไม่ให้ layout ขยายตัวเกินความจำเป็น
#         layout.setContentsMargins(0, 5, 0, 5)
#         layout.setAlignment(Qt.AlignLeft)

#         # เพิ่ม input_widget ลงใน bottomLeftLayout
#         self.bottomLeftLayout.addWidget(input_widget)
#         return input_widget

#     def retranslateUi(self, Widget):
#         Widget.setWindowTitle(QCoreApplication.translate("Widget", u"QNN Trainer", None))

#     def start_training(self):
#         print("Training started...")
#         # QTimer.singleShot(1000, lambda: print("Epoch 1/10 completed"))
#         # QTimer.singleShot(2000, lambda: print("Epoch 2/10 completed"))
#         # QTimer.singleShot(3000, lambda: print("Training completed successfully!"))

# class CustomStream:
#     """คลาสสำหรับ Redirect stdout ไปที่ QTextEdit"""
#     def __init__(self, text_edit):
#         self.text_edit = text_edit

#     def write(self, text):
#         # Append ข้อความและเลื่อนลงไปยังบรรทัดล่างสุด
#         self.text_edit.moveCursor(QTextCursor.End)
#         self.text_edit.insertPlainText(text)
#         self.text_edit.ensureCursorVisible()  # เลื่อนหน้าจออัตโนมัติ

#     def flush(self):
#         QApplication.processEvents()  # ทำให้การแสดงผลเป็นแบบ Real-time

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWidget = QWidget()
#     ui = Ui_Widget()    
#     ui.setupUi(mainWidget)
#     mainWidget.show()
#     sys.exit(app.exec())


# import sys
# from PySide6.QtCore import QCoreApplication, QMetaObject, QTimer, Qt
# from PySide6.QtGui import QFont, QTextCursor
# from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, 
#                                QTextEdit, QWidget, QHBoxLayout, QVBoxLayout, 
#                                QFrame, QComboBox, QGridLayout, QLineEdit, QSizePolicy, QSpacerItem)

# class Ui_Widget(object):
#     def setupUi(self, Widget):
#         Widget.setObjectName("Widget")
#         Widget.resize(1200, 640)

#         # ใช้ GridLayout สำหรับการจัด Layout ทั้งหน้า
#         self.gridLayout = QGridLayout(Widget)

#         # ================== Top Layout ==================
#         self.topLayout = QVBoxLayout()  # ใช้ QVBoxLayout รวมข้อมูลของส่วนบนทั้งหมด
#         #self.topLayout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

#         # ข้อมูลที่เคยอยู่บนซ้าย
#         self.label = QLabel("QNN Trainer")
#         self.label.setFont(QFont("", 25))
#         self.label.setAlignment(Qt.AlignCenter)
#         self.topLayout.addWidget(self.label)

#         self.fileLayout = QHBoxLayout()
#         self.pushButton = QPushButton("Select File")
#         self.pushButton.setFixedWidth(200)
#         self.pushButton.setFont(QFont("", 15))
#         self.fileLayout.addWidget(self.pushButton, alignment=Qt.AlignCenter)

#         self.label_2 = QLabel("No file selected")
#         self.fileLayout.addWidget(self.label_2)

#         self.topLayout.addLayout(self.fileLayout)
#         self.topLayout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

#         self.comboAndApiLayout = QHBoxLayout()
        
#         self.comboBox = QComboBox()
#         self.comboBox.addItems([
#             "Select a backend", "default.qubit", 
#             "Real Quantum Machine", "lightning.qubit", "qiskit.aer"
#         ])
#         self.comboBox.setFont(QFont("", 12))
#         #self.comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.comboBox.setMinimumHeight(25)
#         self.comboAndApiLayout.addWidget(self.comboBox)

#         self.apiLabel = QLabel("API Key:")
#         self.apiLabel.setFont(QFont("", 12))
#         self.comboAndApiLayout.addWidget(self.apiLabel)

#         self.apiInput = QLineEdit()
#         self.apiInput.setFont(QFont("", 12))
#         self.apiInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.comboAndApiLayout.addWidget(self.apiInput)

#         #self.comboAndApiLayout.addSpacerItem(QSpacerItem(20, 250))
#         self.topLayout.addLayout(self.comboAndApiLayout)


#         # เพิ่ม Top Layout ลงใน GridLayout (ครอบคอลัมน์ 2 ช่อง)
#         self.gridLayout.addLayout(self.topLayout, 0, 0, 1, 2)
#         self.topLayout.addItem(QSpacerItem(10, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))

#         # ================== ล่างซ้าย ==================
#         self.bottomLeftLayout = QVBoxLayout()
#         # self.NumOQubInput = self.create_input_section("Number of Qubits:")
#         # self.EpochsInput = self.create_input_section("Epochs:")
#         # self.RepsInput = self.create_input_section("Reps:")
#         # self.TrainSplitInput = self.create_input_section("Train/Test Split (%):")
#         # self.BatchInput = self.create_input_section("Batch Size:")
#         # self.ExportNameInput = self.create_input_section("Exported Model File Name:")
#         self.NumOQubInput, self.NumOQubTextEdit = self.create_input_section("Number of Qubits:")
#         self.EpochsInput, self.EpochsTextEdit = self.create_input_section("Epochs:")
#         self.RepsInput, self.RepsTextEdit = self.create_input_section("Reps:")
#         self.TrainSplitInput, self.TrainSplitTextEdit = self.create_input_section("Train/Test Split (%):")
#         self.BatchInput, self.BatchTextEdit = self.create_input_section("Batch Size:")
#         self.ExportNameInput, self.ExportNameTextEdit = self.create_input_section("Exported Model File Name:")
        

#         for widget in [self.NumOQubInput, self.EpochsInput, self.RepsInput, 
#                        self.TrainSplitInput, self.BatchInput, self.ExportNameInput]:
#             self.bottomLeftLayout.addWidget(widget)

#         self.pushButton_2 = QPushButton("Start Training")
#         self.pushButton_2.setFont(QFont("", 15))
#         self.pushButton_2.setFixedWidth(200)
#         self.pushButton_2.clicked.connect(self.start_training)
#         self.bottomLeftLayout.addWidget(self.pushButton_2, alignment=Qt.AlignCenter)

#         self.gridLayout.addLayout(self.bottomLeftLayout, 1, 0)

#         # ================== ล่างขวา ==================
#         self.bottomRightLayout = QVBoxLayout()
#         self.terminalLabel = QLabel("Terminal Output:")
#         self.terminalLabel.setFont(QFont("", 12))
#         self.bottomRightLayout.addWidget(self.terminalLabel)

#         self.terminalOutput = QTextEdit()
#         self.terminalOutput.setReadOnly(True)
#         self.bottomRightLayout.addWidget(self.terminalOutput)

#         self.gridLayout.addLayout(self.bottomRightLayout, 1, 1)

#         # Redirect stdout ไปที่ QTextEdit
#         sys.stdout = CustomStream(self.terminalOutput)

#         self.retranslateUi(Widget)
#         QMetaObject.connectSlotsByName(Widget)

#     def create_input_section(self, label_text):
#         frame = QFrame()
#         layout = QHBoxLayout(frame)

#         label = QLabel(label_text)
#         label.setFont(QFont("", 12))
#         layout.addWidget(label)

#         textEdit = QTextEdit()
#         textEdit.setFixedHeight(30)
#         textEdit.setFixedWidth(300)
#         layout.addWidget(textEdit)

#         return frame, textEdit

#     def retranslateUi(self, Widget):
#         Widget.setWindowTitle(QCoreApplication.translate("Widget", "QNN Trainer", None))

#     def start_training(self):
#         print("Training started...")
#         try:
#             epochs_text = self.EpochsTextEdit.toPlainText().strip()
#             if not epochs_text:
#                 raise ValueError("Epochs input cannot be empty.")
            
#             epochs = int(epochs_text)
#             print(f"Training for {epochs} epochs...")
#         except ValueError as e:
#             print(f"Invalid input for epochs: {e}")

# class CustomStream:
#     def __init__(self, text_edit):
#         self.text_edit = text_edit

#     def write(self, text):
#         self.text_edit.moveCursor(QTextCursor.End)
#         self.text_edit.insertPlainText(text)
#         self.text_edit.ensureCursorVisible()

#     def flush(self):
#         QApplication.processEvents()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWidget = QWidget()
#     ui = Ui_Widget()
#     ui.setupUi(mainWidget)
#     mainWidget.show()
#     sys.exit(app.exec())


import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QTimer, Qt, QRect
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, 
                               QTextEdit, QWidget, QHBoxLayout, QVBoxLayout, 
                               QFrame, QComboBox, QGridLayout, QLineEdit, QSizePolicy, QSpacerItem)

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(u"Widget")
        Widget.resize(1200, 640)
        self.gridLayout = QGridLayout(Widget)

        # ================== ส่วนกรอกข้อมูลด้านซ้าย ==================
        self.topLayout = QVBoxLayout()

        self.label = QLabel("QNN Trainer")
        self.label.setFont(QFont("", 25))
        self.label.setAlignment(Qt.AlignCenter)
        self.topLayout.addWidget(self.label)

        self.fileLayout = QHBoxLayout()
        self.pushButton = QPushButton("Select File")
        self.pushButton.setFixedWidth(200)
        self.pushButton.setFont(QFont("", 15))
        self.fileLayout.addWidget(self.pushButton, alignment=Qt.AlignCenter)

        self.label_2 = QLabel("No file selected")
        self.fileLayout.addWidget(self.label_2)
        self.topLayout.addLayout(self.fileLayout)
        self.topLayout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        self.comboAndApiLayout = QHBoxLayout()
        self.comboBox = QComboBox()
        self.comboBox.addItems([
            "Select a backend", "default.qubit", 
            "Real Quantum Machine", "lightning.qubit", "qiskit.aer"
        ])
        self.comboBox.setFont(QFont("", 12))
        self.comboBox.setMinimumHeight(25)
        self.comboAndApiLayout.addWidget(self.comboBox)

        # Inputs Section
        self.apiLabel = QLabel("API Key:")
        self.apiLabel.setFont(QFont("", 12))
        self.comboAndApiLayout.addWidget(self.apiLabel)

        self.apiInput = QLineEdit()
        self.apiInput.setFont(QFont("", 12))
        self.apiInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.comboAndApiLayout.addWidget(self.apiInput)

        self.topLayout.addLayout(self.comboAndApiLayout)
        self.gridLayout.addLayout(self.topLayout, 0, 0, 1, 2)
        self.topLayout.addItem(QSpacerItem(10, 100, QSizePolicy.Minimum, QSizePolicy.Fixed))

        self.bottomLeftLayout = QVBoxLayout()
        self.gridLayout.addLayout(self.bottomLeftLayout, 1, 0)

        # Create input sections with QLabel and QTextEdit
        self.NumOQubInput, self.NumOQubEdit = self.create_input_section("Number of Qubits:")
        self.EpochsInput, self.EpochsEdit = self.create_input_section("Epochs:")
        self.TrainSplitInput, self.TrainSplitEdit = self.create_input_section("Train/Test Split (%):")
        self.BatchInput, self.BatchEdit = self.create_input_section("Batch Size:")
        self.RepsInput, self.RepsEdit = self.create_input_section("Reps:")
        self.ExportNameInput, self.ExportNameEdit = self.create_input_section("Exported Model File Name:")
        
        Widget.NumOQubEdit = self.NumOQubEdit
        Widget.EpochsEdit = self.EpochsEdit
        Widget.TrainSplitEdit = self.TrainSplitEdit
        Widget.BatchEdit = self.BatchEdit
        Widget.RepsEdit = self.RepsEdit
        Widget.ExportNameEdit = self.ExportNameEdit

        for widget in [self.NumOQubInput, self.EpochsInput, self.TrainSplitInput,
                       self.BatchInput, self.RepsInput, self.ExportNameInput]:
            self.bottomLeftLayout.addWidget(widget)

        self.pushButton_2 = QPushButton("Start Training")
        self.pushButton_2.setFont(QFont("", 15))
        self.pushButton_2.setFixedWidth(200)
        self.bottomLeftLayout.addWidget(self.pushButton_2, alignment=Qt.AlignCenter)

        # ================== ส่วน Terminal Output ด้านขวา ==================
        self.bottomRightLayout = QVBoxLayout()
        self.terminalOutput = QTextEdit()
        self.terminalOutput.setReadOnly(True)
        self.terminalOutput.setMinimumSize(400, 300)
        self.terminalOutput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottomRightLayout.addWidget(self.terminalOutput)

        self.gridLayout.addLayout(self.bottomRightLayout, 1, 1, 2, 2)

        # Set proportions of columns and rows
        self.gridLayout.setColumnStretch(0, 1)  # Left side (data)
        self.gridLayout.setColumnStretch(1, 3)  # Right side (Terminal)
        self.gridLayout.setRowStretch(0, 1)  # Top row (title and file button)
        self.gridLayout.setRowStretch(1, 4)  # Middle row (data)

        # Redirect stdout to QTextEdit
        sys.stdout = CustomStream(self.terminalOutput)

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

    def create_input_section(self, label_text):
        """Creates a labeled input section with a QTextEdit."""
        input_widget = QWidget()
        layout = QHBoxLayout(input_widget)

        label = QLabel(label_text)
        label.setFont(QFont("", 12))
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        label.setFixedWidth(250)
        layout.addWidget(label)

        lineEdit = QLineEdit()
        lineEdit.setFixedHeight(40)  # Set height for QLineEdit
        lineEdit.setFixedWidth(200)  # Set width for QLineEdit
        layout.addWidget(lineEdit)

        layout.setContentsMargins(0, 5, 0, 5)
        layout.setAlignment(Qt.AlignLeft)

        input_widget.setLayout(layout)  # Set layout for the input widget
        return input_widget, lineEdit

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"QNN Trainer", None))

        
class CustomStream:
    """Class to redirect stdout to QTextEdit."""
    def __init__(self, text_edit):
        self.text_edit = text_edit

    def write(self, text):
        self.text_edit.moveCursor(QTextCursor.End)
        self.text_edit.insertPlainText(text)
        self.text_edit.ensureCursorVisible()

    def flush(self):
        QApplication.processEvents()  # Keep output real-time

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    ui = Ui_Widget()    
    ui.setupUi(mainWidget)
    mainWidget.show()
    sys.exit(app.exec())
