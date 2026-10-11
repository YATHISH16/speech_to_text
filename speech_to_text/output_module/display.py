def display_text(text, metrics):

    print("\n========================")
    print("FINAL TRANSCRIPTION")
    print("========================")

    print(text)

    print("\n===== PERFORMANCE =====")

    print(
        "Processing Time:",
        metrics["processing_time"],
        "seconds"
    )

    print(
        "RTF:",
        metrics["rtf"]
    )