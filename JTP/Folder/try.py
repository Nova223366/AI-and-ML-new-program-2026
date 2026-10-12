from groq_02 import generate_response as k
import pyttsx3
import webbrowser
import time


# ==================== VOICE SETUP ====================

def setup_voice():
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        if voices:
            engine.setProperty("voice", voices[0].id)

        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        return engine

    except Exception as error:
        print(f"Voice initialization failed: {error}")
        return None


engine = setup_voice()


def speak(text):
    """Speak text if voice is available."""
    if engine is None:
        return

    try:
        engine.say(str(text))
        engine.runAndWait()
    except Exception as error:
        print(f"Voice error: {error}")


# ==================== AI RESPONSE ====================

def ask_ai(prompt):
    """Generate an AI response with basic error handling."""
    try:
        response = k(prompt)

        if response is None or not str(response).strip():
            return "Sorry, I received an empty response."

        return str(response)

    except Exception as error:
        print(f"\nAI error: {error}")
        return "Sorry, I couldn't generate a response. Please try again."


# ==================== MAIN MENU ====================

def main():
    print("\n========== MY AI ASSISTANT ==========")
    print("Type 'task'    - School task mode")
    print("Type 'command' - Utility commands")
    print("Type 'help'    - Show available commands")
    print("Type 'exit'    - Quit the assistant")
    print("=====================================\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        command = user_input.lower()

        if not user_input:
            continue

        if command in ("exit", "quit"):
            print("Goodbye!")
            break

        elif command == "task":
            school_tasks()

        elif command == "command":
            utility()

        elif command == "help":
            print(
                "\nAvailable commands:\n"
                "- task: Enter school task mode\n"
                "- command: Open websites\n"
                "- help: Show this help menu\n"
                "- exit: Quit the assistant\n"
            )

        else:
            response = ask_ai(user_input)
            print(f"\nAI: {response}\n")
            speak(response)


# ==================== SCHOOL TASK MODE ====================

def school_tasks():
    animation = [".", "..", "...", "...."]

    for dots in animation:
        print(f"\rLoading{dots}", end="", flush=True)
        time.sleep(0.3)

    print("\n\n======= SCHOOL TASK MODE ACTIVATED =======")
    print("Type 'exit' to return to the main menu.\n")

    while True:
        try:
            school_input = input("Enter your school task: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to the main menu.")
            break

        if school_input.lower() in ("exit", "quit"):
            print("Returning to the main menu...\n")
            break

        if not school_input:
            print("Please enter a school task.")
            continue

        prompt = school_prompt_for_ai(school_input)
        response = ask_ai(prompt)

        print(f"\nAI: {response}\n")
        speak(response)


def school_prompt_for_ai(school_task):
    role = (
        "Act as a friendly high school educator. "
        "Explain the student's task in simple language."
    )

    constraints = """
    Instructions:
    - Explain the concept clearly.
    - Use bullet points where appropriate.
    - Include one simple real-world analogy.
    - Give an example when helpful.
    - Keep the explanation suitable for a high school student.
    """

    return f"{role}\n{constraints}\nStudent's task: {school_task}"


# ==================== UTILITY COMMANDS ====================

def utility():
    websites = {
        "chrome": "https://www.google.com",
        "chatgpt": "https://chatgpt.com",
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
    }

    print("\n========== UTILITY MODE ==========")
    print("Available commands:")

    for name in websites:
        print(f"- open {name}")

    print("- exit (return to main menu)")
    print("==================================\n")

    while True:
        try:
            command = input("Utility: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nReturning to the main menu.\n")
            break

        if command in ("exit", "quit"):
            print("Returning to the main menu.\n")
            break

        if not command:
            continue

        if command.startswith("open "):
            site = command[5:].strip()

            if site in websites:
                try:
                    opened = webbrowser.open(websites[site])

                    if opened:
                        print(f"Opening {site}...")
                    else:
                        print(
                            "The browser may not have opened "
                            "the website automatically."
                        )

                except Exception as error:
                    print(f"Could not open website: {error}")
            else:
                print(f"Unknown website: {site}")

        else:
            print("Unknown command. Type 'help' or 'exit'.")


# ==================== START ASSISTANT ====================

if __name__ == "__main__":
    main()