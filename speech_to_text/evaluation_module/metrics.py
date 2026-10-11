import time

def calculate_processing_time(start_time, end_time):
    return round(end_time - start_time, 2)

def calculate_rtf(audio_duration, processing_time):

    if audio_duration == 0:
        return 0

    return round(processing_time / audio_duration, 2)