import datetime
import random
import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3
import speech_recognition as sr

# --- INITIALIZATION ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# User Configuration
USER_NAME = "Vikram"

# Fun Facts Database
FUN_FACTS = [
    "Honey never spoils; 3,000-year-old edible honey was found in Egyptian tombs!",
    "Bananas are curved because they grow towards the sun against gravity.",
    "Octopuses have three hearts and blue blood.",
    "Venus is the only planet in our solar system that rotates clockwise.",
    "A single strand of spider silk is five times stronger than steel of equal thickness."
]

# --- VOICE ASSISTANT LOGIC ---

def set_voice(gender):
    """Option to change assistant voice (Male / Female)."""
    try:
        if gender == "Female":
            for voice in voices:
                if "female" in voice.name.lower() or "zira" in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    return
            if len(voices) > 1:
                engine.setProperty('voice', voices[1].id)
        else:
            for voice in voices:
                if "male" in voice.name.lower() or "david" in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    return
            if len(voices) > 0:
                engine.setProperty('voice', voices[0].id)
    except Exception as e:
        print(f"Voice switching error: {e}")

def speak(text):
    """Converts text to speech output."""
    output_label.config(text=text)
    root.update()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """Processes recognized user commands."""
    cmd = command.lower()

    # 1. Date Command
    if "date" in cmd:
        today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today's date is {today_date}."

    # 2. Personalized Greeting
    elif any(word in cmd for word in ["hello", "hi", "hey", "greet"]):
        response = f"Hello {USER_NAME}! It's great to assist you today. How can I help?"

    # 3. Random Fun Fact
    elif "fact" in cmd or "fun fact" in cmd:
        fact = random.choice(FUN_FACTS)
        response = f"Here is a fun fact: {fact}"

    # Additional standard command
    elif "time" in cmd:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."

    else:
        response = f"Sorry {USER_NAME}, I recognized '{command}', but I don't have a specific command set for that."

    speak(response)

def listen_and_process():
    """Captures voice input with robust error handling."""
    recognizer = sr.Recognizer()
    status_label.config(text="Status: Listening...", fg="blue")
    root.update()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            status_label.config(text="Status: Processing...", fg="orange")
            root.update()
            
            text = recognizer.recognize_google(audio)
            input_display.config(text=f'You said: "{text}"')
            process_command(text)

    # 4. Robust Error Handling
    except sr.WaitTimeoutError:
        status_label.config(text="Status: Idle", fg="black")
        speak("I didn't hear anything. Please try again.")
    except sr.UnknownValueError:
        status_label.config(text="Status: Idle", fg="black")
        speak("Sorry, I could not understand the audio. Please speak clearly.")
    except sr.RequestError:
        status_label.config(text="Status: Idle", fg="black")
        speak("Could not reach the speech recognition service. Check your internet connection.")
    except Exception as e:
        status_label.config(text="Status: Idle", fg="black")
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    status_label.config(text="Status: Idle", fg="black")

# --- TKINTER GUI BUILD ---

root = tk.Tk()
root.title("Smart Command Pro - Voice Assistant")
root.geometry("450 x 420")
root.configure(bg="#f4f6f9")

# Header Title
title_label = tk.Label(root, text="Smart Command Pro", font=("Helvetica", 16, "bold"), bg="#f4f6f9", fg="#2c3e50")
title_label.pack(pady=10)

# Voice Gender Selection Frame (Requirement 5)
voice_frame = tk.LabelFrame(root, text=" Assistant Voice ", font=("Helvetica", 10, "bold"), bg="#f4f6f9", padx=10, pady=5)
voice_frame.pack(pady=5, fill="x", px=20)

voice_var = tk.StringVar(value="Male")

def update_voice():
    set_voice(voice_var.get())
    speak(f"Voice changed to {voice_var.get()}")

male_rb = tk.Radiobutton(voice_frame, text="Male", variable=voice_var, value="Male", command=update_voice, bg="#f4f6f9")
female_rb = tk.Radiobutton(voice_frame, text="Female", variable=voice_var, value="Female", command=update_voice, bg="#f4f6f9")
male_rb.pack(side="left", expand=True)
female_rb.pack(side="right", expand=True)

# Status & Input Displays
status_label = tk.Label(root, text="Status: Idle", font=("Helvetica", 10, "italic"), bg="#f4f6f9")
status_label.pack(pady=5)

input_display = tk.Label(root, text='You said: "-"', font=("Helvetica", 10), bg="#f4f6f9", fg="#555555", wraplength=380)
input_display.pack(pady=5)

# Assistant Response Output Box
output_frame = tk.LabelFrame(root, text=" Assistant Response ", font=("Helvetica", 10, "bold"), bg="#f4f6f9")
output_frame.pack(pady=10, fill="both", expand=True, px=20)

output_label = tk.Label(output_frame, text="Click 'Speak' to start...", font=("Helvetica", 11), bg="#ffffff", fg="#333333", wraplength=360, justify="left", anchor="nw")
output_label.pack(fill="both", expand=True, padx=10, pady=10)

# Action Button
listen_btn = tk.Button(root, text="🎙️ Click to Speak", font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white", activebackground="#219150", activeforeground="white", command=listen_and_process, padx=20, pady=8)
listen_btn.pack(pady=15)

# Initialize Default Voice
set_voice("Male")

# Run Tkinter Main Loop
root.mainloop()
