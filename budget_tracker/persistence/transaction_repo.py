from budget_tracker.models.transaction import Transaction


class TransactionRepository:
    def __init__(self, connection):
        self.conn = connection

    def add_transaction(self, tx):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (amount, type, category, description, date)
            VALUES (?, ?, ?, ?, ?)
        """, (tx.amount, tx.type, tx.category, tx.description, tx.date))

        self.conn.commit()

    def get_all_transactions(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT amount, type, category, description, date FROM transactions
        """)

        rows = cursor.fetchall()
        return [
            Transaction(
                amount=row[0],
                type=row[1],
                category=row[2],
                description=row[3],
                date=row[4]
            ) for row in rows
        ]