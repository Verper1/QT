# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 569)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(780, 569))
        MainWindow.setMaximumSize(QSize(780, 569))
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet(u"background-color: rgb(146, 157, 255);\n"
"\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 100, 151, 91))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 255, 127);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 210, 151, 91))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 127);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(610, 320, 151, 91))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 101, 101);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 90, 571, 461))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 571, 51))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(610, 500, 151, 51))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Arial\";\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u043d\u043e\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

