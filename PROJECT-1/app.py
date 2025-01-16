import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Rock, Paper, Scissors")

window_width = 500
window_height = 500
root.geometry(f"{window_width}x{window_height}")

choices = [
    ("Rock", "✊"), 
    ("Paper", "✋"), 
    ("Scissors", "✌️")
]


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie! 😊"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You Win! 🎉"
    else:
        return "You Lose! 😢"

def play(user_choice):
    computer_choice = random.choice(choices)[0]
    result = determine_winner(user_choice, computer_choice)
    result_label.config(
        text=f"You chose: {user_choice} {dict(choices)[user_choice]}\n"
             f"Computer chose: {computer_choice} {dict(choices)[computer_choice]}\n{result}"
    )


instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instruction_label.pack(pady=20)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for i, (choice, emoji) in enumerate(choices):
    button = tk.Button(
        button_frame, 
        text=f"{emoji} {choice}", 
        font=("Arial", 14), 
        command=lambda c=choice: play(c)
    )
    button.grid(row=0, column=i, padx=10)


result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
result_label.pack(pady=20)


root.mainloop()
