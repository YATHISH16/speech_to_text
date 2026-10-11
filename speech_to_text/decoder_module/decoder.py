import whisper

model = whisper.load_model("base")


def decode_features(audio_file):

    print("Loading Whisper Model...")

    result = model.transcribe(audio_file)

    text = result["text"]
    language = result["language"]

    # Placeholder confidence value
    confidence = 95.1

    print("Decoding Complete")

    return {
        "text": text,
        "language": language,
        "confidence": confidence
    }