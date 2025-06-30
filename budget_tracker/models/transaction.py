from dataclasses import dataclass

@dataclass
class Transaction:
    amount: float
    type: str
    category: str
    date: str
    description: str = ""

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive.")

        if self.type not in ("income", "expense"):
            raise ValueError("Type must be either 'income' or 'expense'.")

        if self.category == "":
            raise ValueError("Category cannot be empty.")