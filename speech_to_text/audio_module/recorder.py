from scipy.io.wavfile import write
import sounddevice as sd

from audio_module.config import (
    SAMPLING_RATE,
    CHANNELS,
    RECORD_SECONDS,
    OUTPUT_FILE
)

def record_audio():

    print("Speak now...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLING_RATE),
        samplerate=SAMPLING_RATE,
        channels=CHANNELS
    )

    sd.wait()

    write(
        OUTPUT_FILE,
        SAMPLING_RATE,
        audio
    )

    print("Recording saved")

    return OUTPUT_FILE