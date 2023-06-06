import PyInstaller.__main__

PyInstaller.__main__.run([
    '--clean', 
    '-w',
    '-y',
    '--add-data="lib\eng.mp4;lib"',
    '--add-data="lib\sve.mp4;lib"',
    '--add-data="lib\sv.png;lib"',
    '--add-data="lib\gb.png;lib"',
    'video-player.py'
])

#pyinstaller --clean -w -y --add-data="lib\eng.mp4;lib" --add-data="lib\sve.mp4;lib" --add-data="lib\sv.png;lib" --add-data="lib\gb.png;lib" video-player.py
