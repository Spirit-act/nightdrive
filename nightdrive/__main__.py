
from nightdrive.utils import read_file, merge_lists, parse_tracklist, get_files

from subprocess import run
from argparse import ArgumentParser
from os import path
import sys


def main(tracklist: str, file_path: str, output_path: str, album_cover: str|None = None):

    if not path.isdir(output_path):
        sys.tracebacklimit = 0
        raise Exception("Output Folder does not exist. Please create it")

    filelist = merge_lists(
        parse_tracklist(read_file(tracklist)),
        get_files(file_path),
        output_path,
        album_cover
    )


    for item in filelist:
        cmd: str = item.generate_ffmpeg_cmd()
        print(f"execute: {cmd}")
        run(cmd)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="NighDrive Generator",
        description="With this Program you can generate a complete Playlist from Audiofiles and a Tracklist"
    )

    parser.add_argument('-t', '--tracklist', dest="tracklist", required=True)
    parser.add_argument('-f', '--filepath', dest="filepath", required=True)
    parser.add_argument('-o', '--output', dest="outputpath", default="output")
    parser.add_argument('-c', '--cover', dest="cover", required=False)

    args = parser.parse_args()

    main(args.tracklist, args.filepath, args.outputpath, args.cover)