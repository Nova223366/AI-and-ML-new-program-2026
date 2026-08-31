import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language = "en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voice = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voice[0].id)  
    elif language == "es":
        engine.setProperty('voice', voice[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")
    return ""

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def display_menu():
    print("Available translation languages:")
    print("1. Hindi (hi)")
    print("2. tamil (ta)")
    print("3. Spanish (es)")
    print("4. French (fr)")
    print("5. japanese (ja)")
    print("6. German (de)")

    choice = input("Enter the number corresponding to your choice: ") 
    language_map = {
        "1": "hi",
        "2": "ta",
        "3": "es",
        "4": "fr",
        "5": "ja",
        "6": "de"
    }
    return language_map.get(choice, "en")  # Default to English if invalid choice
def main():
    target_language = display_menu()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, target_language)
        speak(translated_text, language=target_language)
        print(f"Original text: {original_text}")

if __name__ == "__main__":
    main()