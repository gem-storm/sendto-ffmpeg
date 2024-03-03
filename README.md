## sendto-ffmpeg
tired of typing output path(s) for ffmpeg? try using sendto-ffmpeg!

### usage
right click your video(s) and select `Send to -> ffmpeg`. a window will open, you type your arguments in, and it'll automatically make the output path for you!

you can also add `-container XYZ` if you would like to use a different container.

### dependencies
- python
- ffmpeg in path

### installation
1. download `main.py`
2. make a new shortcut and make the target follow this:
```
[path/to/python.exe] [path/to/main.py]
```
3. name the shortcut to whatever you'd like, i call it `ffmpeg`
4. move the shortcut to the sendto folder (`%appdata%/microsoft/windows/sendto`)
5. done!
