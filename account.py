class Account:

    def __init__(self, filepath):
        self.path = filepath
        with open(filepath, mode='r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def save(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.path, mode='w') as file:
            file.write(str(self.balance))

account = Account("balance.txt")

account.withdraw(1000)
print(account.balance)

account.commit()
