import soundfile as sf

from preprocessing_module.audio_loader import load_audio
from preprocessing_module.normalizer import normalize_audio
from preprocessing_module.silence_removal import remove_silence

def preprocess_audio(file_path):

    audio, sr = load_audio(file_path)

    audio = normalize_audio(audio)

    audio = remove_silence(audio)

    output_file = "clean_audio.wav"

    sf.write(
        output_file,
        audio,
        sr
    )

    print("Preprocessing complete")

    return output_file