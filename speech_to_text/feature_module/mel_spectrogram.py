import librosa
import numpy as np

def create_mel_spectrogram(audio_file):

    audio, sr = librosa.load(
        audio_file,
        sr=16000
    )

    mel_spec = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=80
    )

    mel_spec_db = librosa.power_to_db(
        mel_spec,
        ref=np.max
    )

    return mel_spec_db