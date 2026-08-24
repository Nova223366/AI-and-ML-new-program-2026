import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language = "en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")

    if language == "en":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in english...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language = "en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return ""

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest = target_language)
    print(f"Translated text: {translation.text}") 
    return translation.text

def display_menu():
    print("Available languages for translation:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Kannada (kn)")
    print("6. Spanish (es)")

    choice = input("Enter the number corresponding to your choice: ")
    language_map = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "kn",
        "6": "es"
    }
    return language_map.get(choice, "en")
def main():
    target_language = display_menu()
    text = speech_to_text()
    if text:
        translated_text = translate_text(text, target_language)
        speak(translated_text, language = target_language)
if __name__ == "__main__":
    main()