# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QListView,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1169, 640)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 20, 191, 51))
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 120, 481, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 110, 191, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 500, 191, 41))
        self.pushButton_2.setFont(font2)
        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(410, 200, 671, 381))
        self.comboBox = QComboBox(Widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 160, 191, 31))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 170, 49, 16))
        self.label_3.setFont(font1)
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(540, 160, 541, 31))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 280, 51, 20))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_4.setFont(font3)
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 330, 141, 20))
        self.label_5.setFont(font3)
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 380, 81, 20))
        self.label_6.setFont(font3)
        self.textEdit_2 = QTextEdit(Widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(280, 270, 81, 31))
        self.textEdit_3 = QTextEdit(Widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(280, 320, 81, 31))
        self.textEdit_4 = QTextEdit(Widget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(280, 370, 81, 31))
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 440, 181, 20))
        self.label_7.setFont(font3)
        self.textEdit_5 = QTextEdit(Widget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(270, 430, 91, 31))
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 230, 101, 20))
        self.textEdit_6 = QTextEdit(Widget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(280, 220, 81, 31))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"QNN Trainer", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"No file selected", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Select file", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Start Training", None))
        
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"default.qubit", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"lightning.qubit", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"qiskit.aer", None))

        self.label_3.setText(QCoreApplication.translate("Widget", u"Api Key:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Epochs:", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Train/Test Split (%):", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Batch Size:", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Exported model file name:", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Number of cubits:", None))
    # retranslateUi

