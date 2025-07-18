from datetime import datetime
import sounddevice as sd

def main():
    print("Hello from meeting-assistant-app!")
    print(datetime.now().strftime('%Y%m%d_%H%M%S'))

    print("Available audio devices:")
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            print(f"{i}: {device['name']} (Input channels: {device['max_input_channels']})")
    print("\nNumber of available audio devices:", len(devices))


if __name__ == "__main__":
    main()
