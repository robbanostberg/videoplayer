# This Python file uses the following encoding: utf-8
import sys
#import urllib.request
#import json
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QStringListModel, QUrl
#from PySide.QtGUI import QGuiApplication
from LangSelectorUI import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.connect()



    sys.exit(app.exec())
