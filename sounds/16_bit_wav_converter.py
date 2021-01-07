import os
import soundfile

# make audio files friendly for 16 bit


def convertAllFilesInDirectoryTo16Bit(directory):
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            nameSolo = file.rsplit(".", 1)[0]
            print(directory + nameSolo)
            data, samplerate = soundfile.read(directory + file)

            soundfile.write(
                "/Users/GCTJZ/OneDrive - Monsanto/Migrated from My PC/Desktop/ARG/sounds/alarms/"
                + nameSolo
                + ".wav",
                data,
                samplerate,
                subtype="PCM_16",
            )
            print("converting " + file + "to 16 - bit")


convertAllFilesInDirectoryTo16Bit(
    "/Users/GCTJZ/OneDrive - Monsanto/Migrated from My PC/Desktop/ARG/sounds/"
)
