import tkinter as tk
from tkinter import ttk, messagebox

from budget_tracker.models.transaction import Transaction
from budget_tracker.persistence.transaction_repo import TransactionRepository
from budget_tracker.persistence.database_manager import create_connection, initialize_database

class BudgetTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")

        # Set up DB connection
        self.conn = create_connection()
        initialize_database(self.conn)
        self.repo = TransactionRepository(self.conn)

        # Build the UI
        self.build_form()

    def build_form(self):
        # Amount
        tk.Label(self.root, text="Amount:").grid(row=0, column=0, sticky="e")
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        # Type
        tk.Label(self.root, text="Type:").grid(row=1, column=0, sticky="e")
        self.type_var = tk.StringVar(value="expense")
        self.type_menu = ttk.Combobox(self.root, textvariable=self.type_var, values=["expense", "income"])
        self.type_menu.grid(row=1, column=1)

        # Category
        tk.Label(self.root, text="Category:").grid(row=2, column=0, sticky="e")
        self.category_entry = tk.Entry(self.root)
        self.category_entry.grid(row=2, column=1)

        # Description
        tk.Label(self.root, text="Description:").grid(row=3, column=0, sticky="e")
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=3, column=1)

        # Date
        tk.Label(self.root, text="Date (YYYY-MM-DD):").grid(row=4, column=0, sticky="e")
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=4, column=1)

        # Submit Button
        submit_btn = tk.Button(self.root, text="Add Transaction", command=self.submit_transaction)
        submit_btn.grid(row=5, columnspan=2, pady=10)

    def submit_transaction(self):
        try:
            tx = Transaction(
                amount=float(self.amount_entry.get()),
                type=self.type_var.get(),
                category=self.category_entry.get(),
                description=self.description_entry.get(),
                date=self.date_entry.get()
            )
            self.repo.add_transaction(tx)
            messagebox.showinfo("Success", "Transaction added successfully!")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
