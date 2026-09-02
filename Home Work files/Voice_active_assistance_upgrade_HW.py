import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random

VOICE_ID = 1  # Change to 0 for another available voice
USER_SPEECH_RATE = 150
user_name = ""


def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    if VOICE_ID < len(voices):
        engine.setProperty("voice", voices[VOICE_ID].id)

    engine.setProperty("rate", USER_SPEECH_RATE)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""

    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""


def respond_to_command(command):
    global user_name

    if "hello" in command:
        speak(f"Hello {user_name}! How can I assist you today?")

    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")

    elif "date" in command:
        today = datetime.now().date()
        speak(f"Today's date is {today}.")

    elif "my name is" in command:
        user_name = command.split("my name is", 1)[1].strip()
        speak(f"Nice to meet you, {user_name}!")

    elif "fact" in command:
        facts = [
            "Honey never spoils.",
            "Bananas are berries, but strawberries are not.",
            "A day on Venus is longer than a year on Venus.",
            "Octopuses have three hearts.",
            "There are more stars in the universe than grains of sand on Earth."
        ]
        speak(random.choice(facts))

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Have a great day!")
        return False

    else:
        speak("I'm sorry, I don't have a response for that command.")

    return True


def main():
    global user_name

    speak("Hello! I am your voice assistant. What is your name?")

    user_name = get_audio()

    while True:
        command = get_audio()

        if command:
            continue_running = respond_to_command(command)

            if not continue_running:
                break


if __name__ == "__main__":
    main()