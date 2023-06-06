#from pynput import keyboard as k, mouse as m
import os
#os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import tkinter as tk
from time import sleep
#import cv2
#import screeninfo as si
import vlc

#from LangSelector.UntitledProject.main import start
#python -m PyQt6.uic.pyuic -o LangSelectorUI.py -x LangSelector.ui


global media_player

'''from PyQt6 import QtCore, QtWidgets


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
        Form.setWindowTitle(_translate("Form", "Sound Player"))'''


def start():
    pass
    '''import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
    '''
test = True
bw = 20
bh = int(bw/2)
ratio = str(15 * bw) + "x" + str(15 * bh)

def eng(temp):
    global v
    media_player = vlc.MediaPlayer()
# media object
    media = vlc.Media("en.mp4")
# setting media to the media player
    media_player.set_media(media)
# toggling full screen
    if not test:
        media_player.toggle_fullscreen()
# start playing video
    
    media_player.play()
 
# wait so the video can be played for 5 seconds
# irrespective for length of video
    sleep(2)#180+35
    media_player.stop()
    #msg() '''


    enmp.play()
    print("eng")
    sleep(5)
    while enmp.is_playing():
        sleep(1)

def sve(temp):
    media_player = vlc.MediaPlayer()
# media object
    media = vlc.Media("sv.mp4")
# setting media to the media player
    media_player.set_media(media)
# toggling full screen
    if not test:
        media_player.toggle_fullscreen()
# start playing video
    media_player.play()
 
# wait so the video can be played for 5 seconds
# irrespective for length of video
    #sleep(3)#180+35
    for i in range(10):
        print(media_player.get_state())
        sleep(1)
    #media_player.stop()
    
        

w = tk.Tk()
global v
#v = tk.Tk()
#w.geometry(ratio)
'''en = tk.Button(w,text="eng", image=tk.PhotoImage(file="gb.png")) # height=bh, width=bw,
en.image = tk.PhotoImage(file="gb.png")
#en.pack(in_=w, side="right")
en.grid(in_=w, row=0, column=1)
en.bind('<Button-1>', eng)
sv = tk.Button(w,text="sve", image=tk.PhotoImage(file="sv.png"))
sv.grid(in_=w, row=0, column=0)
#sv.pack(in_=w, side="left")
sv.bind('<Button-1>', sve)'''
#global m
#m = []
#for i in si.get_monitors():
#    m.append([i.is_primary, i.x, i.y, i.width, i.height])
global enmp
global svmp
global enml
global svml
enmp = vlc.MediaListPlayer()
svmp = vlc.MediaListPlayer()
svi = vlc.Instance()
eni = vlc.Instance()
svml = svi.media_list_new()
enml = eni.media_list_new()
sv = svi.media_new("sv.mp4")
en = eni.media_new("en.mp4")
aaen = eni.media_new("aa.mp4")
aasv = svi.media_new("aa.mp4")
enmp.set_media_list(enml)
svmp.set_media_list(svml)
#clr = en.cget("bg")
w.mainloop()
#start()