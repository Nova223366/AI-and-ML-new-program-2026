import tkinter as tk
import random
from colorama import init

init(autoreset=True)

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x450")
window.config(bg="#f0f0f0")

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

def play(user_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}"
    )

    score_label.config(
        text=f"Score\nYou: {player_score}  Computer: {computer_score}"
    )

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=20)

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack()

tk.Button(frame, text="Rock", width=12, command=lambda: play("Rock")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Paper", width=12, command=lambda: play("Paper")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Scissors", width=12, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)

score_label = tk.Label(window, text="Score\nYou: 0  Computer: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=10)

def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text="Score\nYou: 0  Computer: 0")
    result_label.config(text="")

tk.Button(window, text="Reset Game", command=reset, bg="red", fg="white").pack(pady=10)

window.mainloop()