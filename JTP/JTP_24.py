import datetime
import random
import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr


# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------

engine = pyttsx3.init()
voices = engine.getProperty("voices")


# --------------------------------------------------
# FUN FACTS DATABASE
# --------------------------------------------------

FUN_FACTS = [
    "Honey never spoils; 3,000-year-old edible honey was found in Egyptian tombs!",
    "Bananas are curved because they grow towards the sun against gravity.",
    "Octopuses have three hearts and blue blood.",
    "Venus is the only planet in our solar system that rotates clockwise.",
    "A single strand of spider silk is five times stronger than steel of equal thickness."
]


# --------------------------------------------------
# VOICE ASSISTANT LOGIC
# --------------------------------------------------

def get_user_name():
    """Get the current user's name from the input field."""
    name = name_entry.get().strip()
    return name if name else "Friend"


def set_voice(gender):
    """Change the assistant voice to male or female when available."""
    try:
        if not voices:
            return

        if gender == "Female":
            for voice in voices:
                voice_name = voice.name.lower()

                if "female" in voice_name or "zira" in voice_name:
                    engine.setProperty("voice", voice.id)
                    return

            # Fallback
            if len(voices) > 1:
                engine.setProperty("voice", voices[1].id)
            else:
                engine.setProperty("voice", voices[0].id)

        else:
            for voice in voices:
                voice_name = voice.name.lower()

                if "male" in voice_name or "david" in voice_name:
                    engine.setProperty("voice", voice.id)
                    return

            # Fallback
            engine.setProperty("voice", voices[0].id)

    except Exception as e:
        print(f"Voice switching error: {e}")


def speak(text):
    """Convert text to speech and display it."""
    output_label.config(text=text)
    root.update_idletasks()

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")


def process_command(command):
    """Process recognized voice commands."""
    cmd = command.lower().strip()
    user_name = get_user_name()

    # Date command
    if "date" in cmd:
        today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today's date is {today_date}."

    # Greeting
    elif any(word in cmd.split() for word in ["hello", "hi", "hey", "greet"]):
        response = (
            f"Hello {user_name}! "
            "It's great to assist you today. How can I help?"
        )

    # Fun fact
    elif "fact" in cmd:
        fact = random.choice(FUN_FACTS)
        response = f"Here is a fun fact: {fact}"

    # Time
    elif "time" in cmd:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."

    # Unknown command
    else:
        response = (
            f"Sorry {user_name}, I recognized '{command}', "
            "but I don't have a specific command set for that."
        )

    speak(response)


def listen_and_process():
    """Capture voice input and process it."""
    recognizer = sr.Recognizer()

    status_label.config(text="Status: Listening...", fg="blue")
    root.update_idletasks()

    try:
        with sr.Microphone() as source:

            # Reduce background-noise problems
            recognizer.adjust_for_ambient_noise(source, duration=0.8)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        status_label.config(text="Status: Processing...", fg="orange")
        root.update_idletasks()

        text = recognizer.recognize_google(audio)

        input_display.config(
            text=f'You said: "{text}"'
        )

        process_command(text)

    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")

    except sr.UnknownValueError:
        speak(
            "Sorry, I could not understand the audio. "
            "Please speak clearly."
        )

    except sr.RequestError:
        speak(
            "Could not reach the speech recognition service. "
            "Check your internet connection."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"An unexpected error occurred:\n{str(e)}"
        )

    finally:
        status_label.config(
            text="Status: Idle",
            fg="black"
        )


# --------------------------------------------------
# GUI
# --------------------------------------------------

root = tk.Tk()

root.title("Smart Command Pro - Voice Assistant")
root.geometry("450x480")
root.configure(bg="#f4f6f9")
root.resizable(False, False)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

title_label = tk.Label(
    root,
    text="Smart Command Pro",
    font=("Helvetica", 16, "bold"),
    bg="#f4f6f9",
    fg="#2c3e50"
)

title_label.pack(pady=10)


# --------------------------------------------------
# USER PROFILE
# --------------------------------------------------

name_frame = tk.LabelFrame(
    root,
    text=" User Profile ",
    font=("Helvetica", 10, "bold"),
    bg="#f4f6f9",
    padx=10,
    pady=5
)

name_frame.pack(
    pady=5,
    fill="x",
    padx=20
)


name_label = tk.Label(
    name_frame,
    text="Enter Your Name:",
    font=("Helvetica", 10),
    bg="#f4f6f9"
)

name_label.pack(
    side="left",
    padx=5
)


name_entry = tk.Entry(
    name_frame,
    font=("Helvetica", 10)
)

name_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)

name_entry.insert(0, "User")


# --------------------------------------------------
# VOICE SELECTION
# --------------------------------------------------

voice_frame = tk.LabelFrame(
    root,
    text=" Assistant Voice ",
    font=("Helvetica", 10, "bold"),
    bg="#f4f6f9",
    padx=10,
    pady=5
)

voice_frame.pack(
    pady=5,
    fill="x",
    padx=20
)


voice_var = tk.StringVar(value="Male")


def update_voice():
    """Update selected assistant voice."""
    selected_voice = voice_var.get()
    set_voice(selected_voice)
    speak(f"Voice changed to {selected_voice}")


male_rb = tk.Radiobutton(
    voice_frame,
    text="Male",
    variable=voice_var,
    value="Male",
    command=update_voice,
    bg="#f4f6f9"
)

male_rb.pack(
    side="left",
    expand=True
)


female_rb = tk.Radiobutton(
    voice_frame,
    text="Female",
    variable=voice_var,
    value="Female",
    command=update_voice,
    bg="#f4f6f9"
)

female_rb.pack(
    side="right",
    expand=True
)


# --------------------------------------------------
# STATUS
# --------------------------------------------------

status_label = tk.Label(
    root,
    text="Status: Idle",
    font=("Helvetica", 10, "italic"),
    bg="#f4f6f9"
)

status_label.pack(pady=5)


# --------------------------------------------------
# USER INPUT DISPLAY
# --------------------------------------------------

input_display = tk.Label(
    root,
    text='You said: "-"',
    font=("Helvetica", 10),
    bg="#f4f6f9",
    fg="#555555",
    wraplength=380
)

input_display.pack(pady=5)


# --------------------------------------------------
# ASSISTANT RESPONSE
# --------------------------------------------------

output_frame = tk.LabelFrame(
    root,
    text=" Assistant Response ",
    font=("Helvetica", 10, "bold"),
    bg="#f4f6f9"
)

output_frame.pack(
    pady=10,
    fill="both",
    expand=True,
    padx=20
)


output_label = tk.Label(
    output_frame,
    text="Click 'Speak' to start...",
    font=("Helvetica", 11),
    bg="#ffffff",
    fg="#333333",
    wraplength=360,
    justify="left",
    anchor="nw"
)

output_label.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# --------------------------------------------------
# LISTEN BUTTON
# --------------------------------------------------

listen_btn = tk.Button(
    root,
    text="🎙️ Click to Speak",
    font=("Helvetica", 12, "bold"),
    bg="#27ae60",
    fg="white",
    activebackground="#219150",
    activeforeground="white",
    command=listen_and_process,
    padx=20,
    pady=8
)

listen_btn.pack(pady=15)


# --------------------------------------------------
# DEFAULT VOICE
# --------------------------------------------------

set_voice("Male")


# --------------------------------------------------
# START APPLICATION
# --------------------------------------------------

root.mainloop()
