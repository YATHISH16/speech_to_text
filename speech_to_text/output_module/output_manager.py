from output_module.display import display_text
from output_module.printer import print_status


def show_output(text, metrics):

    print("\n========================")
    print("FINAL TRANSCRIPTION")
    print("========================\n")

    print(text)

    print("\n===== PERFORMANCE =====")

    print(
        f"Detected Language : {metrics['language']}"
    )

    print(
        f"Confidence        : {metrics['confidence']:.1f}%"
    )

    print(
        f"Processing Time   : {metrics['processing_time']:.2f} sec"
    )

    print(
        f"Latency           : {metrics['latency']:.2f} sec"
    )

    print(
        f"RTF               : {metrics['rtf']:.2f}"
    )

    print("\nOutput Generated Successfully")