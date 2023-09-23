# from pydub import AudioSegment
from pydub import utils, AudioSegment


def get_prober_name():
    return "B:/ffmpeg-master-latest-win64-gpl/bin/ffprobe.exe"


AudioSegment.converter = "B:/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"
utils.get_prober_name = get_prober_name
song = AudioSegment.from_mp3("testing.mp3")
# Open an mp3 file
# song = AudioSegment.from_file("D:/KABAKOO/Projects/cut/testing.mp3",format="mp3")

# pydub does things in milliseconds
# ten_seconds = 10 * 1000

# song clip of 10 seconds from starting
# first_10_seconds = song[:ten_seconds]

# start and end time
start_min = 0
start_sec = 10
end_min = 0
end_sec = 30

# pydub does things in milliseconds, so convert time
start = ((start_min * 60) + start_sec) * 1000
end = ((end_min * 60) + end_sec) * 1000

# song clip of 10 seconds from starting
first_10_seconds = song[start: end]

# save file
first_10_seconds.export("first_10_seconds.mp3",
                        format="mp3")
print("New Audio file is created and saved")