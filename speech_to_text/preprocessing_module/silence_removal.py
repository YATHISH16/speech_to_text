import librosa

def remove_silence(audio):

    intervals = librosa.effects.split(
        audio,
        top_db=20
    )

    return librosa.effects.remix(
        audio,
        intervals
    )