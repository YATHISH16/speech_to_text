import numpy as np

def normalize_audio(audio):

    return audio / np.max(np.abs(audio))