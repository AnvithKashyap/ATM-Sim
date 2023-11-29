import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Simulator")
        self.master.geometry("400x300")
        self.balance = 1000
        self.create_widgets()

    def create_widgets(self):
        # Balance Label
        self.balance_label = tk.Label(self.master, text="Balance: ${}".format(self.balance))
        self.balance_label.pack(pady=10)

        self.amount_entry = tk.Entry(self.master, width=20)
        self.amount_entry.pack(pady=10)

        self.check_balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance)
        self.check_balance_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

    def update_balance_label(self):
        self.balance_label.config(text="Balance: ${}".format(self.balance))

    def check_balance(self):
        messagebox.showinfo("Balance", "Your balance is ${}".format(self.balance))

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                self.update_balance_label()
                messagebox.showinfo("Withdraw", "Withdrawal successful. Your new balance is ${}".format(self.balance))
            else:
                messagebox.showerror("Error", "Invalid amount or insufficient balance.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                self.update_balance_label()
                messagebox.showinfo("Deposit", "Deposit successful. Your new balance is ${}".format(self.balance))
            else:
                messagebox.showerror("Error", "Invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    atm_simulator = ATM(root)
    root.mainloop()
