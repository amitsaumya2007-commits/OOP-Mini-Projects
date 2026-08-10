class Account:
    def __init__(self,owner:str, balance:float = 0.0) -> None:
        self.owner = owner
        self._balance = balance
        self._transaction_history = []

    @property
    def balance(self):
        return self._balance
    @property
    def transaction_history(self):
        return self._transaction_history
    
    def deposit(self,amount:float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount
        self._transaction_history.append(f"Deposited: {amount}")

    def withdraw(self,amount:float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance.")
        self._balance -= amount
        self._transaction_history.append(f"Withdrawl: {amount}")
    def transfer(self,account_name:Account, amount:float):
        self.withdraw(amount)
        account_name.deposit(amount)
    def __repr__(self):
        return f"Account(owner= {self.owner}, balance= {self.balance})"

account = Account("Saumya",1000)
account2 = Account("Akhilesh",1000)
account.transfer(account2,50)
print(account.balance, account2.balance)
print(account.transaction_history)

# Defining a getter only for a attribute( not setter), makes that attribute read-only and now,
# you cannot modify that attribute once it is set-up. If you tried to do so,  you will get an
# AttributeError