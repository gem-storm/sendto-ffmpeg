from os.path import splitext
from subprocess import run

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("video")
args = parser.parse_args()

input_video = args.video.replace('"', "")


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

run(
    f'ffmpeg -i "{input_video}" {remove_container(enc_args)} "{splitext(input_video)[0]} ~ Encoded.{container(enc_args)}"'
)
