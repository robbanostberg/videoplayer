# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LangSelector.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        Form.setStyleSheet(u"QWidget {\n"
"	background: rgb(109, 109, 109);}")
        self.btn_sv = QPushButton(Form)
        self.btn_sv.setObjectName(u"btn_sv")
        self.btn_sv.setGeometry(QRect(70, 210, 500, 300))
        self.btn_sv.setStyleSheet(u"QPushButton {image: url(:/content/sv.jpg)}")
        self.btn_en = QPushButton(Form)
        self.btn_en.setObjectName(u"btn_en")
        self.btn_en.setGeometry(QRect(700, 210, 500, 300))
        self.btn_en.setStyleSheet(u"QPushButton {image: url(:/content/gb.jpg)}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sound Player", None))
        self.btn_sv.setText("")
        self.btn_en.setText("")
    # retranslateUi

