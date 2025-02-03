import tkinter as tk

from tkinter import messagebox

import random



class NumberGuessingGame:

    def __init__(self, master):

        self.master = master

        master.title("Number Guessing Game")



        self.label = tk.Label(master, text="Guess the number between 1 and 100")

        self.label.pack()



        self.entry = tk.Entry(master)

        self.entry.pack()



        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)

        self.submit_button.pack()



        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)

        self.new_game_button.pack()



        self.number = random.randint(1, 100)

        self.guesses = 0



    def check_guess(self):

        try:

            guess = int(self.entry.get())

            self.guesses += 1

            if guess < self.number:

                messagebox.showinfo("Result", "Too low! Try again.")

            elif guess > self.number:

                messagebox.showinfo("Result", "Too high! Try again.")

            else:

                messagebox.showinfo("Result", f"Congratulations! You guessed it in {self.guesses} tries.")

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number.")



    def new_game(self):

        self.number = random.randint(1, 100)

        self.guesses = 0

        self.entry.delete(0, tk.END)

        messagebox.showinfo("New Game", "A new game has started. Guess the number!")



if __name__ == "__main__":

    root = tk.Tk()

    game = NumberGuessingGame(root)

    root.mainloop()
