from os import listdir

from nightdrive.models import AudioFile, Track, MergedFile

def read_file(path: str) -> str:
    with open(path, 'r', encoding="utf8") as file:
        return file.read()

def parse_tracklist(data: str) -> list[Track]:
    tracks = []
    for index, line in enumerate(data.split("\n")):
        tracks.append(Track(index + 1, line))
    return tracks

def get_files(path: str) -> list[AudioFile]:
    files = []
    for file in listdir(path):
        files.append(AudioFile(file, path))
    return files

def merge_lists(tracklist: list[Track], fileslist: list[AudioFile], album_cover: str|None = None):
    merged_files: list[MergedFile] = []
    for index, track in enumerate(tracklist):
        audiofile: AudioFile = fileslist[index]
        if (audiofile.id is None):
            continue
        merged_files.append(MergedFile(track, audiofile, len(tracklist), album_cover))
    return merged_files