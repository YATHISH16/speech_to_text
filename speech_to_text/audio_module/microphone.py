import sounddevice as sd

def list_microphones():
    print(sd.query_devices())

def check_microphone():
    devices = sd.query_devices()

    if len(devices) > 0:
        print("Microphone detected")
        return True

    print("No microphone found")
    return False