# from pydub import AudioSegment
from pydub import utils, AudioSegment
from datasets import load_dataset

def get_prober_name():
    return "B:/ffmpeg-master-latest-win64-gpl/bin/ffprobe.exe"


print("Loading datasets ...")

bambara = load_dataset('csv', data_files={'train': 'train.csv'})

bambara_train = bambara["train"]
# print(bambara_train.to_list()) # give format : {path: "", sentence: ""}[]


AudioSegment.converter = "B:/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe"
utils.get_prober_name = get_prober_name
song = AudioSegment.from_wav("griots_r1_2.wav")
#song = AudioSegment.from_file("griots_r1_2.wav", format="wav")


# pydub does things in milliseconds
for element in bambara_train:
    arr1 = element['path'].split("PLAGE-")
    arr2 = arr1[1].split(".wav")
    arr3 = arr2[0].split("-")
    print(arr3)
    start = float(arr3[0]) * 1000
    end = float(arr3[1]) * 1000
    result = song[start:end]
    # print(start)
    # print(end)
    # save file
    result.export(element['path'], format="mp3")
    print(element['path'] + " saved !")





# start and end time
# start_min = 0
# start_sec = 10
# end_min = 0
# end_sec = 30
# pydub does things in milliseconds, so convert time
# start = ((start_min * 60) + start_sec) * 1000
# end = ((end_min * 60) + end_sec) * 1000