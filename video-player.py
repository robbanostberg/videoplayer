import os
#os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
import tkinter as tk
import tkinter.font as font
from time import sleep
import vlc
import pywinauto as pwa
import win32gui
import sys

global media_player
global lastLang
#global handle

test = 0
short = 0
scale = 0.25
lastLang = -1

def eng(temp=None):
    global media_player
    global lastLang
    lastLang = 1
    #media_player = vlc.MediaPlayer()
    if short:
        media = vlc.Media("lib/en.mp4")
    else:
        media = vlc.Media("lib/eng.mp4")
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
    if short:
        media = vlc.Media("lib/sv.mp4")
    else:
        media = vlc.Media("lib/sve.mp4")
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

'''def getAppHandle(temp=0):
    win = pwa.findwindows.find_windows(title_re="VLC")
    #print(win)
    #win = win32gui.EnumWindows()
    return win

def actPlayer(temp=0):
    global handle
    win32gui.SetForegroundWindow(handle)
    '''

def play(lang=-1): # 0 = swedish, 1 = english, 2 = play a paused video, 3 = pause, 4 = restart, 5 = close player
    global media_player
    #print(media_player.get_state())
    #state = [media_player.get_state()==vlc.State.Error, media_player.get_state()==vlc.State.Ended,
     #         media_player.get_state()==vlc.State.Opening, media_player.get_state()==vlc.State.Paused, 
      #        media_player.get_state()==vlc.State.Playing, media_player.get_state()==vlc.State.Stopped]
    #print(state, lang)
    if not media_player.get_state()==vlc.State.Playing and (lang == 0 or lang == 1) :
        #print("play")
        if lang == 0:
            sve()
        elif lang == 1:
            eng()
    elif media_player.get_state()==vlc.State.Paused and lang == 2:
        #print("unpause")
        media_player.set_pause(0)
    elif media_player.get_state()==vlc.State.Playing and lang == 3:
        #print("pause")
        media_player.set_pause(1)
    elif lang == 4:
        #print("restart")
        if lastLang == 0:
            sve()
        elif lastLang == 1:
            eng()
    elif lang == 5:
        #print("stop")
        media_player.stop()

def admin(temp=0):
    #print('yippie!')
    global pauseb
    global playb
    global restartb
    global closeb
    global actb
    global hideb

    pauseb.grid(row=2, column=2, pady=20)
    playb.grid(row=2, column=1, pady=20)
    restartb.grid(row=3, column=2, pady=20)
    closeb.grid(row=3, column=1, pady=20)
    actb.grid(row=4, column=1, pady=20)
    hideb.grid(row=4, column=2, pady=20)

def hide(temp=0):
    global pauseb
    global playb
    global restartb
    global closeb
    global actb
    global hideb

    pauseb.grid_forget()
    playb.grid_forget()
    restartb.grid_forget()
    closeb.grid_forget()
    actb.grid_forget()
    hideb.grid_forget()

def closeP(temp=0):
    sys.exit(0)

w = tk.Tk()
w.title('Video Player')
width, height = w.winfo_screenwidth(), w.winfo_screenheight()
if width > 1920 or height > 1080:
    width, height = 1920, 1080
#print(width, height)
w.configure(bg='black')
media_player = vlc.MediaPlayer()
#handle = getAppHandle()
svi = tk.PhotoImage(file="lib/sv.png")
eni = tk.PhotoImage(file="lib/gb.png")
svb = tk.Button(w, image = svi, command=svbtn)
enb = tk.Button(w, image = eni, command=enbtn)
space = tk.Label(w, width=int(width/200), height=int(height/50))
space.configure(bg='black')
space.grid(row=0, column=0)
space.bind('<Button-3>', admin) # right mouse button
space.bind('<Button-2>', admin) # right mouse button or maybe middle btn?
svb.grid(row=1, column=1, padx=150, pady=10)
enb.grid(row=1, column=2, padx=150, pady=10)
svb.image = svi
enb.image = eni

global pauseb
global playb
global restartb
global closeb
global actb
global hideb

pauseb = tk.Button(w, text="Pause", command=pausebtn)
playb = tk.Button(w, text="Play", command=playbtn)
restartb = tk.Button(w, text="Restart", command=restartbtn)
closeb = tk.Button(w, text="Close")
closeb.bind('<Button-1>', closebtn)
closeb.bind('<Button-2>', closeP)
closeb.bind('<Button-3>', closeP)
actb = tk.Button(w, text= "Activate" ''', command=actPlayer''')
hideb = tk.Button(w, text="Hide", command=hide)

bfont = font.Font(size=20)
btns = [pauseb, playb, restartb, closeb, actb, hideb]

for btn in btns:
    btn['font'] = bfont

width, height = w.winfo_screenwidth(),w.winfo_screenheight()
w.geometry('%dx%d%+d+%d'%(width, height, width - 8, -31)) # width x height + xpad + ypad

w.resizable(False, False)



w.mainloop()