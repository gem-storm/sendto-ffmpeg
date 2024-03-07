presets = {
    "H264": "-c:v libx264 -preset slow -aq-mode 3 -crf 16",
    "HEVC": "-c:v libx265 -preset medium -x265-params aq-mode=3:no-sao=1 -crf 20",
    "UTVIDEO": "-c:v utvideo",
    "4K": "-vf scale=3840:-2:flags=neighbor",
    "FLAC": "-c:a flac -container flac",
    "MP3": "-c:a mp3 -b:a 320k -container mp3",
    "ACOPY": "-c:a copy",
    "VCOPY": "-c:v copy",
    "DEFAULT": "-c:v libx264 -preset slow -aq-mode 3 -crf 16 -c:a copy",
}

# add your own! make sure to end each line with a comma (,)
# keep them in ALL CAPS so regular arguments don't get replaced
# "DEFAULT" will automatically apply if no arguments are typed


from os.path import splitext
from subprocess import run
from sys import argv


if len(argv) == 1:
    vids = input(
        "no input videos were passed. paste the path(s) here separated by a comma and space (,):\n>>>"
    ).split(", ")
    input_videos = [vid.replace('"', "") for vid in vids]
else:
    input_videos = argv[1:]


def container(ffmpeg_args):
    if "-container" in ffmpeg_args:
        split_args = ffmpeg_args.split("-container ", 2)[1].strip()
        return split_args.split(" ", 1)[0].replace('"', "")
    elif "utvideo" in ffmpeg_args:
        return "mkv"
    return "mp4"


def log(ffmpeg_args):
    if "-log" in ffmpeg_args:
        return True
    return False


def suffix(ffmpeg_args):
    if "-suffix" in ffmpeg_args:
        split_args = ffmpeg_args.split("-suffix", 2)[1].strip()
        return " ".join(split_args.split(" ")[:-1]).replace('"', "")
    return "~ Encoded"


def preset(ffmpeg_args, presets):
    for key, value in presets.items():
        if key in ffmpeg_args:
            ffmpeg_args = ffmpeg_args.replace(key, value)
    return ffmpeg_args


def fix_args(args_preset):
    args_suffix = args_preset.replace(f'-suffix "{suffix(args_preset)}"', "")
    args_log = args_suffix.replace("-log", "")
    new_args = args_log.replace(f"-container {container(args_log)}", "")
    # i cant think of any way to do this better sry
    if new_args.strip():
        return new_args
    return presets["DEFAULT"]


enc_args = input("args:\n>>>")

for v in input_videos:
    args_preset = preset(enc_args, presets)
    if log(enc_args):
        with open("log.txt", "w") as file:
            file.write(
                f'ffmpeg -i "{v}" {fix_args(args_preset)} "{splitext(v)[0]}{suffix(args_preset)}.{container(args_preset)}"\n'
            )
    run(
        f'ffmpeg -i "{v}" {fix_args(args_preset)} "{splitext(v)[0]}{suffix(args_preset)}.{container(args_preset)}"'
    )
