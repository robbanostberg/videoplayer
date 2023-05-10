import os
#os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
import tkinter as tk
from tkinter import ttk
from time import sleep
import vlc
import pywinauto as pwa
import win32gui

global media_player
global lastLang
global handle

test = True
scale = 0.25
lastLang = -1

def eng(temp=None):
    global media_player
    global lastLang
    lastLang = 1
    #media_player = vlc.MediaPlayer()
    media = vlc.Media("en.mp4")
    media_player.set_media(media)
    if not test:
        media_player.toggle_fullscreen()
    else:
        media_player.video_set_scale(scale)
    media_player.play()

def sve(temp=None):
    global media_player
    global lastLang
    lastLang = 0
    #media_player = vlc.MediaPlayer()
    #media_player.play()
    media = vlc.Media("sv.mp4")
    media_player.set_media(media)
    if not test:
        media_player.toggle_fullscreen()
    else:
        media_player.video_set_scale(scale)
    media_player.play()

def svbtn(temp=0):
    play(0)

def enbtn(temp=0):
    play(1)

def playbtn(temp=0):
    play(2)

def pausebtn(temp=0):
    play(3)

def restartbtn(temp=0):
    play(4)

def closebtn(temp=0):
    play(5)

def getAppHandle(temp=0):
    win = pwa.findwindows.find_windows(title_re="VLC")
    print(win)
    #win = win32gui.EnumWindows()
    return win

def actPlayer(temp=0):
    global handle
    win32gui.SetForegroundWindow(handle)
    

def play(lang=-1): # 0 = swedish, 1 = english, 2 = play a paused video, 3 = pause, 4 = restart, 5 = close player
    global media_player

    state = [media_player.get_state()==vlc.State.Error, media_player.get_state()==vlc.State.Ended,
              media_player.get_state()==vlc.State.Opening, media_player.get_state()==vlc.State.Paused, 
              media_player.get_state()==vlc.State.Playing, media_player.get_state()==vlc.State.Stopped]
    print(state, lang)
    if not media_player.get_state()==vlc.State.Playing and (lang == 0 or lang == 1) :
        print("play")
        if lang == 0:
            sve()
        elif lang == 1:
            eng()
    elif media_player.get_state()==vlc.State.Paused and lang == 2:
        print("unpause")
        media_player.set_pause(0)
    elif media_player.get_state()==vlc.State.Playing and lang == 3:
        print("pause")
        media_player.set_pause(1)
    elif lang == 4:
        print("restart")
        if lastLang == 0:
            sve()
        elif lastLang == 1:
            eng()
    elif lang == 5:
        print("stop")
        media_player.stop()

w = tk.Tk()
media_player = vlc.MediaPlayer()
handle = getAppHandle()
svi = tk.PhotoImage(file="sv.png")
eni = tk.PhotoImage(file="gb.png")
svb = tk.Button(w, image = svi, command=svbtn)
enb = tk.Button(w, image = eni, command=enbtn)
svb.grid(row=0, column=0, padx=10, pady=10)
enb.grid(row=0, column=1, padx=10, pady=10)
svb.image = svi
enb.image = eni

pauseb = tk.Button(w, text="Pause", command=pausebtn)
playb = tk.Button(w, text="Play", command=playbtn)
restartb = tk.Button(w, text="Restart", command=restartbtn)
closeb = tk.Button(w, text="Close", command=closebtn)
actb = tk.Button(w, text= "Activate", command=actPlayer)
pauseb.grid(row=1, column=1)
playb.grid(row=1, column=0)
restartb.grid(row=2, column=1)
closeb.grid(row=2, column=0)
actb.grid(row=3, column=0)


w.mainloop()