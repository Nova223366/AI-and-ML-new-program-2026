import random, pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_samples():
    samples = [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Greetings! How may I help you?",
        "Hey! What would you like to talk about?",
        "Good day! How can I be of service?"
    ]
    return samples

def main():
    print("Ai voice lab")
    speak("Hello! I am your AI voice assistant. How can I help you today?")

    while True:
        text = input("\n You: ").strip().lower()

        if text == 'exit':
            speak("Goodbye! Have a great day!")
            break

        elif text == 'sample':
            phrase = random.choice(get_samples())
            speak(phrase)

        elif text == 'speed up':
            current_rate = engine.getProperty("rate")+50
            engine.setProperty("rate", current_rate)
            speak(f"Speech rate increased to {current_rate} words per minute.")

        elif text == 'slow down':
            current_rate = engine.getProperty("rate")-50
            engine.setProperty("rate", current_rate)
            speak(f"Speech rate decreased to {current_rate} words per minute.")

        elif text == 'increase volume':
            current_volume = engine.getProperty("volume")+0.1
            if current_volume > 1.0:
                current_volume = 1.0
            engine.setProperty("volume", current_volume)
            speak(f"Volume increased to {int(current_volume * 100)} percent.")

        elif text == 'decrease volume':
            current_volume = engine.getProperty("volume")-0.1
            if current_volume < 0.0:
                current_volume = 0.0
            engine.setProperty("volume", current_volume)
            speak(f"Volume decreased to {int(current_volume * 100)} percent.")

        elif text == 'tell a joke':
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "Why did the bicycle fall over? Because it was two-tired!",
                "Why did the math book look sad? Because it had too many problems.",
                "Why did the computer go to the doctor? Because it caught a virus!"
            ]
            joke = random.choice(jokes)
            speak(joke)

        else:
            print("Type 'sample for ideas or 'exit' to quit.")
            speak("I didn't quite catch that.Try again")

if __name__ == "__main__":
    main()
