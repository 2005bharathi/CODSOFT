import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    message = f"You chose {player_choice}\nComputer chose {computer_choice}\n\nResult: {result}"
    messagebox.showinfo("Result", message)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    window = tk.Tk()
    window.title("Rock, Paper, Scissors Game")

    rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
    paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
    scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))

    rock_button.pack(pady=10)
    paper_button.pack(pady=10)
    scissors_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
