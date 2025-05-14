# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowWuUTAs.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.ipAddressLineEdit = QLineEdit(self.centralwidget)
        self.ipAddressLineEdit.setObjectName(u"ipAddressLineEdit")

        self.verticalLayout_2.addWidget(self.ipAddressLineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.portLineEdit = QLineEdit(self.centralwidget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.portLineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.startServerBtn = QPushButton(self.centralwidget)
        self.startServerBtn.setObjectName(u"startServerBtn")

        self.horizontalLayout.addWidget(self.startServerBtn)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.sendBtn = QPushButton(self.centralwidget)
        self.sendBtn.setObjectName(u"sendBtn")

        self.gridLayout.addWidget(self.sendBtn, 1, 2, 1, 1)

        self.filePathLineEdit = QLineEdit(self.centralwidget)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.filePathLineEdit, 1, 1, 1, 1)

        self.logsTextBrowser = QTextBrowser(self.centralwidget)
        self.logsTextBrowser.setObjectName(u"logsTextBrowser")

        self.gridLayout.addWidget(self.logsTextBrowser, 4, 0, 1, 3)

        self.selectFileBtn = QPushButton(self.centralwidget)
        self.selectFileBtn.setObjectName(u"selectFileBtn")
        self.selectFileBtn.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.selectFileBtn, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.startServerBtn.setText(QCoreApplication.translate("MainWindow", u"Start Server", None))
        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.selectFileBtn.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
    # retranslateUi

