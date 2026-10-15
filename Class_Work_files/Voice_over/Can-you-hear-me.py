import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    stop_event.set()

def spinner():
    spinner_chars = '|/-\\'
    idx = 0
    while not stop_event.is_set():
        sys.stdout.print('\rRecording... ' + spinner_chars[idx % len(spinner_chars)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write('\rRecording stopped.\n')

def record_until_enter():
    p = pyaudio.PyAudio()
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    frmes_per_buffer = 1024

    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=frmes_per_buffer)
    frames = []

    threading.Thread(target=wait_for_enter).start()
    threading.Thread(target=spinner).start()

    while not stop_event.is_set():
        try:
            data = stream.read(frmes_per_buffer)
            frames.append(data)
        except Exception as e:
            print(f"Error while recording: {e}")
            break

    stream.stop_stream()
    stream.close()
    sample_width = p.get_sample_size(format)
    p.terminate()

    audio_data = b''.join(frames)
    return audio_data, sample_width, rate

def save_audio(data, rate, width, filename = "audio.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"Audio saved to {filename}")

def transcribe_audio(data, rate, width, filename = "trascription.txt"):
    recognizer = sr.Recognizer()
    audio_data = AudioData(data, rate, width)
    try:
        text = recognizer.recognize_google(audio_data)
        with open(filename, 'w') as f:
            f.write(text)
        print(f"Transcription saved to {filename}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    print("Transcription process completed.")
    with open(filename, 'w') as f:
        f.write(text)
    print(f"Saved transcription to {filename}")

def show_waveform(data, rate):
    audio_array = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(audio_array) / rate, num=len(audio_array))
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_array)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def main():
    print("Starting audio recording. Press Enter to stop.")
    audio_data, sample_width, rate = record_until_enter()
    save_audio(audio_data, rate, sample_width)
    transcribe_audio(audio_data, rate, sample_width)
    show_waveform(audio_data, rate)

if __name__ == "__main__":
    main()