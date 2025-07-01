import tkinter as tk
from budget_tracker.ui.main_app_ui import BudgetTrackerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()
