#from pynput import keyboard as k, mouse as m
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import tkinter as tk
from time import sleep
import cv2
from screeninfo import get_monitors, Monitor
import vlc
#import libvlc.dll

global media_player

def eng(temp):
    global v
    media_player = vlc.MediaPlayer()
# media object
    media = vlc.Media("en.mp4")
# setting media to the media player
    media_player.set_media(media)
# toggling full screen
    media_player.toggle_fullscreen()
# start playing video
    
    media_player.play()
 
# wait so the video can be played for 5 seconds
# irrespective for length of video
    sleep(2)#180+35)
    media_player.stop()
    msg()

    '''
    enmp.play()
    print("eng")
    sleep(5)
    while enmp.is_playing():
        sleep(1)'''

def sve(temp):
    media_player = vlc.MediaPlayer()
# media object
    media = vlc.Media("sv.mp4")
# setting media to the media player
    media_player.set_media(media)
# toggling full screen
    media_player.toggle_fullscreen()
# start playing video
    media_player.play()
 
# wait so the video can be played for 5 seconds
# irrespective for length of video
    #sleep(3)#180+35)
    for i in range(10):
        print(media_player.get_state())
        sleep(1)
    #media_player.stop()
    
        

w = tk.Tk()
global v
#v = tk.Tk()
w.geometry("150x30")
en = tk.Button(w,text="eng")
en.pack(in_=w, side="right")
en.bind('<Button-1>', eng)
sv = tk.Button(w,text="sve")
sv.pack(in_=w, side="left")
sv.bind('<Button-1>', sve)
global m
m = []
for i in get_monitors():
    m.append([i.is_primary, i.x, i.y, i.width, i.height])
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