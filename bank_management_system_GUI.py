import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                return f"${amount} deposited. New balance: ${self.balance}"
            else:
                return "Deposit amount must be positive."
        except ValueError:
            return "Invalid amount entered. Please enter a number."

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if 0 < amount <= self.balance:
                self.balance -= amount
                return f"${amount} withdrawn. New balance: ${self.balance}"
            else:
                return "Insufficient funds or invalid amount."
        except ValueError:
            return "Invalid amount entered. Please enter a number."

    def check_balance(self):
        return f"Account balance: ${self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added: ${interest}. New balance: ${self.balance}"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if 0 < amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                return f"${amount} withdrawn. New balance: ${self.balance}"
            else:
                return "Overdraft limit exceeded or invalid amount."
        except ValueError:
            return "Invalid amount entered. Please enter a number."

class BankingApp:
    def __init__(self, root):
        self.accounts = {}
        self.root = root
        self.root.title("Banking System")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Banking System", font=('Helvetica', 16, 'bold')).grid(row=0, columnspan=2, pady=10)

        tk.Button(self.root, text="Create Account", command=self.create_account).grid(row=1, column=0, pady=5)
        tk.Button(self.root, text="Deposit Money", command=self.deposit_money).grid(row=2, column=0, pady=5)
        tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money).grid(row=3, column=0, pady=5)
        tk.Button(self.root, text="Check Balance", command=self.check_balance).grid(row=4, column=0, pady=5)
        tk.Button(self.root, text="Add Interest", command=self.add_interest_to_savings).grid(row=5, column=0, pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=6, column=0, pady=5)

    def create_account(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Create Account")

        tk.Label(self.top, text="Account Type (savings/checking):").grid(row=0, column=0, pady=5)
        self.account_type = tk.Entry(self.top)
        self.account_type.grid(row=0, column=1, pady=5)

        tk.Label(self.top, text="Account Number:").grid(row=1, column=0, pady=5)
        self.account_number = tk.Entry(self.top)
        self.account_number.grid(row=1, column=1, pady=5)

        tk.Label(self.top, text="Account Holder:").grid(row=2, column=0, pady=5)
        self.account_holder = tk.Entry(self.top)
        self.account_holder.grid(row=2, column=1, pady=5)

        tk.Label(self.top, text="Initial Deposit:").grid(row=3, column=0, pady=5)
        self.initial_deposit = tk.Entry(self.top)
        self.initial_deposit.grid(row=3, column=1, pady=5)

        tk.Button(self.top, text="Create", command=self.save_account).grid(row=4, columnspan=2, pady=5)

    def save_account(self):
        account_type = self.account_type.get().strip().lower()
        account_number = self.account_number.get().strip()
        account_holder = self.account_holder.get().strip()
        try:
            initial_deposit = float(self.initial_deposit.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Invalid initial deposit amount. Please enter a number.")
            return

        if account_type == "savings":
            account = SavingsAccount(account_number, account_holder, initial_deposit)
        elif account_type == "checking":
            account = CheckingAccount(account_number, account_holder, initial_deposit)
        else:
            messagebox.showerror("Error", "Invalid account type. Please try again.")
            return

        self.accounts[account_number] = account
        messagebox.showinfo("Success", f"{account_type.capitalize()} account created for {account_holder} with account number {account_number}.")
        self.top.destroy()

    def deposit_money(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Deposit Money")

        tk.Label(self.top, text="Account Number:").grid(row=0, column=0, pady=5)
        self.account_number = tk.Entry(self.top)
        self.account_number.grid(row=0, column=1, pady=5)

        tk.Label(self.top, text="Amount to Deposit:").grid(row=1, column=0, pady=5)
        self.amount = tk.Entry(self.top)
        self.amount.grid(row=1, column=1, pady=5)

        tk.Button(self.top, text="Deposit", command=self.save_deposit).grid(row=2, columnspan=2, pady=5)

    def save_deposit(self):
        account_number = self.account_number.get().strip()
        amount = self.amount.get().strip()

        if account_number in self.accounts:
            message = self.accounts[account_number].deposit(amount)
            messagebox.showinfo("Info", message)
            self.top.destroy()
        else:
            messagebox.showerror("Error", "Account not found. Please try again.")

    def withdraw_money(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Withdraw Money")

        tk.Label(self.top, text="Account Number:").grid(row=0, column=0, pady=5)
        self.account_number = tk.Entry(self.top)
        self.account_number.grid(row=0, column=1, pady=5)

        tk.Label(self.top, text="Amount to Withdraw:").grid(row=1, column=0, pady=5)
        self.amount = tk.Entry(self.top)
        self.amount.grid(row=1, column=1, pady=5)

        tk.Button(self.top, text="Withdraw", command=self.save_withdraw).grid(row=2, columnspan=2, pady=5)

    def save_withdraw(self):
        account_number = self.account_number.get().strip()
        amount = self.amount.get().strip()

        if account_number in self.accounts:
            message = self.accounts[account_number].withdraw(amount)
            messagebox.showinfo("Info", message)
            self.top.destroy()
        else:
            messagebox.showerror("Error", "Account not found. Please try again.")

    def check_balance(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Check Balance")

        tk.Label(self.top, text="Account Number:").grid(row=0, column=0, pady=5)
        self.account_number = tk.Entry(self.top)
        self.account_number.grid(row=0, column=1, pady=5)

        tk.Button(self.top, text="Check", command=self.show_balance).grid(row=1, columnspan=2, pady=5)

    def show_balance(self):
        account_number = self.account_number.get().strip()

        if account_number in self.accounts:
            balance = self.accounts[account_number].check_balance()
            messagebox.showinfo("Balance", balance)
            self.top.destroy()
        else:
            messagebox.showerror("Error", "Account not found. Please try again.")

    def add_interest_to_savings(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Add Interest")

        tk.Label(self.top, text="Account Number:").grid(row=0, column=0, pady=5)
        self.account_number = tk.Entry(self.top)
        self.account_number.grid(row=0, column=1, pady=5)

        tk.Button(self.top, text="Add Interest", command=self.apply_interest).grid(row=1, columnspan=2, pady=5)

    def apply_interest(self):
        account_number = self.account_number.get().strip()

        if account_number in self.accounts:
            account = self.accounts[account_number]
            if isinstance(account, SavingsAccount):
                message = account.add_interest()
                messagebox.showinfo("Info", message)
                self.top.destroy()
                messagebox.showerror("Error", "This operation is only available for savings accounts.")
        else:
            messagebox.showerror("Error", "Account not found. Please try again.")

def main():
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

