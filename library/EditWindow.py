# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(282, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(282, 533))
        Dialog.setMaximumSize(QSize(282, 533))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 470, 111, 51))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 255, 127);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 400, 241, 51))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 127);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 470, 111, 51))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 101, 101);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 241, 31))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 90, 221, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 130, 221, 101))
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMouseTracking(True)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.dateTimeEdit = QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(80, 240, 121, 51))
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setMinimumDateTime(QDateTime(QDate(2025, 1, 8), QTime(0, 0, 0)))
        self.dateTimeEdit.setCalendarPopup(True)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 310, 139, 74))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"font: 700 9pt \"Arial\";")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"font: 700 9pt \"Arial\";")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"font: 700 9pt \"Arial\";")

        self.verticalLayout.addWidget(self.radioButton_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439 \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u0438\u0437\u043a\u0438\u0439 \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
    # retranslateUi

