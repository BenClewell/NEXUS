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
                "/Users/Ben/Desktop/python projects/NEXUS/sounds/wav_exports/"
                + nameSolo
                + ".wav",
                data,
                samplerate,
                subtype="PCM_16",
            )
            print("converting " + file + "to 16 - bit")


convertAllFilesInDirectoryTo16Bit(
    "/Users/Ben/Desktop/python projects/NEXUS/sounds/"
)
