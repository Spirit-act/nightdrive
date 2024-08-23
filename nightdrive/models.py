class Model:
    def __repr__(self) -> str:
        return str(self.__dict__)

class Track(Model):
    def __init__(self, id: int, data: str) -> None:
        self.id: int = id
        elements: list = data.split(" ", 1)[1].split(" - ")
        self.interpret: str = elements.pop(0)
        self.title: str =  " - ".join(elements)

class AudioFile(Model):
    def __init__(self, file_name: str, path: str) -> None:
        self.file_name: str = file_name
        self.path: str = path
        self.parse_title(file_name.split(".")[0])

    def parse_title(self, full_title: str):
        elements: list = full_title.split(" - ")
        self.interpret = elements[0]
        self.album = elements[1]
        self.id = None
        if (len(elements) > 2):
            self.id = int(elements[2].split(" ")[0])

class MergedFile(Model):
    def __init__(self, track: Track, file: AudioFile, list_size: int, album_cover: str|None = None) -> None:
        self.path: str = file.path + "/" + file.file_name
        self.file_name: str = file.file_name
        self.interpret: str = track.interpret
        self.album: str = file.album
        self.id: str = file.id
        self.title: str = track.title.replace("\"", "\\\"")
        self.track_count = list_size
        self.album_cover = album_cover

    def generate_ffmpeg_cmd(self) -> str:
        metadata: str = f'-metadata title="{self.title}" -metadata author="{self.interpret}" -metadata album="{self.album}" -metadata track={self.id}/{self.track_count} -metadata artist="Skeler" -metadata genre="Phonk/Wave"'
        album_cover: str = f''
        if self.album_cover:
            album_cover = f'-i {self.album_cover} -c copy -disposition:v attached_pic'
        return f'ffmpeg.exe -i "{self.path}" {album_cover} {metadata} "output/{self.file_name}"'
