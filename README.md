## sendto-ffmpeg
tired of typing output path(s) for ffmpeg? try using sendto-ffmpeg!


### usage
right click your video(s) and select `Send to -> ffmpeg`. a window will open, you type your arguments in, and it'll automatically run the command for you! (no need for typing any paths!)


### dependencies
- python (preferably in path)
- ffmpeg (must be in path)
you can install both of these easily using [scoop](https://scoop.sh):
```powershell
scoop.cmd install python
scoop.cmd install ffmpeg
```


### installation
1. download `main.py`
2. make a new shortcut and make the target follow this:
```
[path/to/python.exe] [path/to/main.py]
```
3. name the shortcut to whatever you'd like, i call it `ffmpeg`
4. move the shortcut to the sendto folder (`%appdata%/microsoft/windows/sendto`)
5. done!


### misc. arguments
1. add `-container "XYZ"` while typing your arguments to specify the output container. e.g. `-container "mkv"`. default depends on codec.
2. adding `-log` will write the ffmpeg command(s) to a file called `log.txt` in the sendto folder.
3. adding `-suffix "XYZ"` will change the suffix applied to the filename. e.g. `-suffix " - h264"`. defaults to ` ~ Encoded`.


### presets
at the top of `main.py`, you can add your own argument presets, for example:
```py
presets = {
    "H264": "-c:v libx264 -preset slow -aq-mode 3 -crf 16",
}
```
a few are included by default. if the value before `:` is in your args, it will automatically be replaced with the value after `:`.

you can also make a preset called `"DEFAULT"` which will apply if no arguments are given.

syntax:
- it's recommended to keep the first value in all caps, so regular arguments aren't replaced by accident.
- make sure to end each line with `,` or python won't recognize the ones following (and will prob crash).
- make sure all keys and values are surrounded by quotes (`'` or `"`).