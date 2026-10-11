import time

from audio_module.microphone import check_microphone
from audio_module.recorder import record_audio

from preprocessing_module.preprocessor import preprocess_audio

from feature_module.feature_extractor import extract_features

from encoder_module.encoder import encode_features

from decoder_module.decoder import decode_features

from language_module.language_processor import process_text

from output_module.output_manager import show_output

from storage_module.storage import save_transcript

from evaluation_module.evaluator import evaluate


def main():

    print("\n===== SPEECH TO TEXT SYSTEM =====\n")

    if not check_microphone():
        print("Microphone not detected!")
        return

    # Start Timer
    start_time = time.time()

    # Step 1: Record Audio
    audio_file = record_audio()

    # Step 2: Preprocess Audio
    clean_file = preprocess_audio(audio_file)

    # Step 3: Feature Extraction
    features = extract_features(clean_file)

    # Step 4: Encoder
    encoded_features = encode_features(features)

    # Step 5: Decoder
    decoded_result = decode_features(clean_file)

    decoded_text = decoded_result["text"]
    detected_language = decoded_result["language"]
    confidence = decoded_result["confidence"]

    # Convert language code to full name
    language_map = {
        "ta": "Tamil",
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "ml": "Malayalam",
        "kn": "Kannada"
    }

    detected_language = language_map.get(
        detected_language,
        detected_language
    )

    # Step 6: Language Processing
    final_text = process_text(decoded_text)

    # Stop Timer
    end_time = time.time()

    # Step 7: Evaluation
    metrics = evaluate(
        start_time=start_time,
        end_time=end_time,
        audio_duration=5
    )

    metrics["language"] = detected_language
    metrics["confidence"] = confidence

    # Step 8: Save Transcript
    save_transcript(final_text)

    # Step 9: Display Output
    show_output(final_text, metrics)

    print("\nSystem Execution Completed")


if __name__ == "__main__":
    main()