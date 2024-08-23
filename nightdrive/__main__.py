
from nightdrive.utils import read_file, merge_lists, parse_tracklist, get_files

from subprocess import run
from argparse import ArgumentParser


def main(tracklist: str, file_path: str, album_cover: str|None = None):
    filelist = merge_lists(
        parse_tracklist(read_file(tracklist)),
        get_files(file_path),
        album_cover
    )


    for item in filelist:
        cmd: str = item.generate_ffmpeg_cmd()
        print(f"run {cmd}")
        run(cmd)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="NighDrive Generator",
        description="With this Program you can generate a complete Playlist from Audiofiles and a Tracklist"
    )

    parser.add_argument('-t', '--tracklist', dest="tracklist", required=True)
    parser.add_argument('-f', '--filepath', dest="filepath", required=True)
    parser.add_argument('-c', '--cover', dest="cover", required=False)

    args = parser.parse_args()

    main(args.tracklist, args.filepath, args.cover)