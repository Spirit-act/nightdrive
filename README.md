# Generate Skeler NightDrive Playlists

## Requirements

- All Audio Files from the Video
- Tracklist
- Python >= 3.8
- ffmpeg

## Download the Audio Files

```shell
yt-dlp -f ba[ext=m4a] --split-chapters https://www.youtube.com/watch?v=<watch_id>
```

## Tracklist

look in the comments of the NightDrive Videos and copy everything in a `tracklist.txt`

! No NewLine at the end of the File

## Execution

### minimal

```shell
python -m nightdrive -t tracklist.txt -f path/to/the/folder/with/all/audio/files
```

### with album cover

```shell
python -m nightdrive -t tracklist.txt -f path/to/the/folder/with/all/audio/files -c path/to/the/album/cover/image.png
```