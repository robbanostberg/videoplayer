# Form implementation generated from reading ui file 'LangSelector.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        Form.setStyleSheet("QWidget {\n"
"    background: rgb(109, 109, 109);}")
        self.btn_sv = QtWidgets.QPushButton(parent=Form)
        self.btn_sv.setGeometry(QtCore.QRect(70, 210, 500, 300))
        self.btn_sv.setStyleSheet("QPushButton {image: url(:/content/sv.jpg)}")
        self.btn_sv.setText("")
        self.btn_sv.setObjectName("btn_sv")
        self.btn_en = QtWidgets.QPushButton(parent=Form)
        self.btn_en.setGeometry(QtCore.QRect(700, 210, 500, 300))
        self.btn_en.setStyleSheet("QPushButton {image: url(:/content/gb.jpg)}")
        self.btn_en.setText("")
        self.btn_en.setObjectName("btn_en")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sound Player"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
