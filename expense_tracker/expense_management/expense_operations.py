import sqlite3
class Manager:
    def __init__(self,name= "Manager"):
        self.name = name

    def __str__(self):
        return self.name

class ExpenseManager(Manager):

    def __init__(self,db,name="ExpenseManager"):
        super().__init__(name)
        self.db = db

    def add_expense(self, payer, amount, participants):
        participants_str = ",".join(participants) #each participants sperated by a comma
        # need keep track of the definition of participants
        # either the payer is involved or not for calculating balances

        # Insert expense
        self.db.cursor.execute("""
            INSERT INTO expenses (payer, amount, participants)
            VALUES (?, ?, ?)
        """, (payer, amount, participants_str))

        self.db.conn.commit()
        return f"Expense of {amount} added for {payer}, split among {participants}."

    def list_expenses(self):
        self.db.cursor.execute("SELECT * FROM expenses")
        return self.db.cursor.fetchall()

    def remove_expense(self, expense_id):
        # Fetch participants and payer for the expense
        self.db.cursor.execute("SELECT payer, amount, participants FROM expenses WHERE id = ?", (expense_id,))
        expense = self.db.cursor.fetchone()
        if not expense:
            return f"Expense with ID {expense_id} does not exist."

        self.db.cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self.db.conn.commit()
        return f"Expense with ID {expense_id} removed successfully."

    def settle_debt(self, payer: str, receiver: str, amount: float):
        """
        Settle a portion of the debt by recording a payment from the payer to the receiver.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        try:
            #self.db.cursor.execute("UPDATE balances SET balance = balance + ? WHERE user = ?", (amount, receiver))
            #self.db.cursor.execute("UPDATE balances SET balance = balance - ? WHERE user = ?", (amount, payer))
            self.db.cursor.execute("select * from debts where creditor = ? and debtor = ?",(receiver, payer))
            if_exist_users = self.db.cursor.fetchone()
            if not if_exist_users:
                raise ValueError("receiver or payer does not exist.")
            self.db.cursor.execute("UPDATE debts SET amount = amount - ? where creditor = ? and debtor = ?",
            (amount,receiver,payer))
            # Commit changes
            self.db.conn.commit()
            return print(f"Payment of {amount:.2f} from {payer} to {receiver} recorded successfully.")

        except Exception as e:
            self.db.conn.rollback()
            raise e


