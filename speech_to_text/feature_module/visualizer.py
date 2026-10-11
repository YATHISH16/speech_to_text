import librosa.display
import matplotlib.pyplot as plt

def show_spectrogram(mel_spec):

    plt.figure(figsize=(10,4))

    librosa.display.specshow(
        mel_spec,
        x_axis='time',
        y_axis='mel'
    )

    plt.colorbar()

    plt.title("Mel Spectrogram")

    plt.tight_layout()

    plt.show()