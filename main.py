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
        return split_args.split(" ", 1)[0]
    elif "utvideo" in ffmpeg_args:
        return "mkv"
    return "mp4"


def remove_container(ffmpeg_args):
    return ffmpeg_args.replace("-container " + container(ffmpeg_args), "")


enc_args = input("args:\n>>>")

for v in input_videos:
    run(
        f'ffmpeg -i "{v}" {remove_container(enc_args)} "{splitext(v)[0]} ~ Encoded.{container(enc_args)}"'
    )
