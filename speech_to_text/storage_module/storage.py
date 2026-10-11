from storage_module.file_manager import write_to_file


def save_transcript(text):

    filename = "transcript.txt"

    write_to_file(text, filename)

    print("Transcript Saved Successfully")

    return filename