import random
import tkinter as tk
from tkinter import simpledialog, messagebox


class NumberGuessGame:
    def __init__(self, master):
        self.master = master
        master.title("Sonni topish o'yini")

        self.lower_label = tk.Label(master, text="Quyi chegarani kiriting:",bg='light green')
        self.lower_label.pack()

        self.lower_entry = tk.Entry(master,border=5)
        self.lower_entry.pack()

        self.upper_label = tk.Label(master, text="Yuqori chegarani kiriting:",bg='light green')
        self.upper_label.pack()

        self.upper_entry = tk.Entry(master,border=5)
        self.upper_entry.pack()

        self.start_button = tk.Button(master, text="O'yinni boshlash", command=self.start_game,borderwidth=5)
        self.start_button.pack()

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

    def random_number_return(self, a, b):
        return random.randint(a, b)

    def input_number(self):
        while True:
            try:
                return int(tk.simpledialog.askstring("Enter Number", "Taxmin soningizni kiriting:"))
            except ValueError:
                messagebox.showerror("Error", "Xato son kiritingiz!")

    def game(self, lower, upper):
        cnt1, cnt2 = 0, 0
        random_number = self.random_number_return(lower, upper)

        while True:
            number = self.input_number()

            if random_number > number:
                self.result_text.insert(tk.END, f"Kompyuter o'ylagan son {number} kattaroq!\n")
                cnt2 += 1
                
            elif random_number < number:
                self.result_text.insert(tk.END, f"Kompyuter o'ylagan son {number} kichikroq!\n")
                cnt2 += 1
                
            else:
                self.result_text.insert(tk.END, "Tabriklayman! Siz topdingiz!\n")
                cnt1 += 1
                response = messagebox.askquestion("Play Again", "Qayta o'ynashni xohlaysizmi?")

                if response == "no":
                    break

                lower, upper = map(int, tk.simpledialog.askstring("Enter Range", "Enter the new range (lower upper):").split())
                random_number = self.random_number_return(lower, upper)

        total_attempts = cnt1 + cnt2
        self.result_text.insert(tk.END, f"Total attempts: {total_attempts}, Correct guesses: {cnt1}\n")

    def start_game(self):
        lower = int(self.lower_entry.get())
        upper = int(self.upper_entry.get())
        self.game(lower, upper)


if __name__ == '__main__':
    root = tk.Tk()
    app = NumberGuessGame(root)
    root.mainloop()
