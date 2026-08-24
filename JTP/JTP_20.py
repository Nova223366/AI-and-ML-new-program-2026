import speech_recognition as sr
import pyttsx3
from googletrans import Translator


# ---------------- TEXT TO SPEECH ----------------

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    voices = engine.getProperty("voices")

    # Language names used by Windows voices
    language_names = {
        "en": ["english", "david", "zira", "mark"],
        "hi": ["hindi", "hemant", "kalpana"],
        "ta": ["tamil", "valluvar"],
        "te": ["telugu", "chitra"],
        "bn": ["bengali", "bengali"],
        "kn": ["kannada"],
        "es": ["spanish", "sabina", "helena"]
    }

    selected_voice = None

    # Find the voice for the selected language
    for voice in voices:
        voice_info = (
            str(voice.name) + " " +
            str(voice.id) + " " +
            str(voice.languages)
        ).lower()

        for name in language_names.get(language, ["english"]):
            if name in voice_info:
                selected_voice = voice.id
                break

        if selected_voice:
            break

    # Use the selected voice
    if selected_voice:
        engine.setProperty("voice", selected_voice)
        print("Voice selected successfully.")
    else:
        print("⚠️ Voice for", language, "not found.")
        print("Using default Windows voice.")

    engine.say(text)
    engine.runAndWait()


# ---------------- SPEECH TO TEXT ----------------

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None


# ---------------- TRANSLATION ----------------

def translate_text(text, target_language):
    translator = Translator()

    translation = translator.translate(
        text,
        dest=target_language
    )

    print(f"Translated text: {translation.text}")

    return translation.text


# ---------------- LANGUAGE MENU ----------------

def display_menu():

    print("\nAvailable languages for translation:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Kannada (kn)")
    print("6. Spanish (es)")

    choice = input(
        "Enter the number corresponding to your choice: "
    )

    language_map = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "kn",
        "6": "es"
    }

    return language_map.get(choice, "en")


# ---------------- MAIN PROGRAM ----------------

def main():

    target_language = display_menu()

    text = speech_to_text()

    if text:

        translated_text = translate_text(
            text,
            target_language
        )

        speak(
            translated_text,
            language=target_language
        )


if __name__ == "__main__":
    main()