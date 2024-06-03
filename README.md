# Bank-Managemrnt-System-Using-GUI-coded-in-Python
This script is a simple banking application implemented using Python's Tkinter library for the graphical user interface (GUI). The application allows users to create and manage bank accounts, including savings and checking accounts, and perform various banking operations.

Key Features:
Bank Account Classes:

BankAccount: A base class for handling basic account operations such as deposit, withdrawal, and balance check.
SavingsAccount: Inherits from BankAccount and adds the ability to accumulate interest.
CheckingAccount: Inherits from BankAccount and allows withdrawals up to an overdraft limit.
Banking Operations:

Deposit Money: Users can deposit funds into their accounts.
Withdraw Money: Users can withdraw funds from their accounts within the available balance or overdraft limit.
Check Balance: Users can view the current balance of their accounts.
Add Interest: Users can add interest to savings accounts.
Graphical User Interface:

Main Window: Contains buttons to access different functionalities like creating an account, depositing money, withdrawing money, checking balance, and adding interest.
Dialogs and Forms: Separate windows (top-level dialogs) are used for each operation, prompting the user for necessary information such as account type, account number, account holder name, deposit amount, withdrawal amount, etc.
Usage:
Creating an Account: Users select the account type (savings or checking), enter the account number, account holder's name, and initial deposit amount.
Depositing Money: Users provide the account number and the amount to be deposited.
Withdrawing Money: Users provide the account number and the amount to be withdrawn.
Checking Balance: Users enter the account number to view the current balance.
Adding Interest: Users provide the account number for the savings account to apply interest.
Error Handling:
The application includes error handling mechanisms:

Validates deposit and withdrawal amounts to ensure they are numeric and positive.
Checks for sufficient funds during withdrawal and ensures the overdraft limit is not exceeded.
Verifies that account numbers exist before performing operations.
Displays appropriate error messages for invalid inputs or operations.
Main Function:
The main() function initializes the Tkinter root window and creates an instance of the BankingApp class, starting the GUI event loop.

This application provides a straightforward interface for managing basic banking tasks, making it suitable for educational purposes or simple banking simulations.
