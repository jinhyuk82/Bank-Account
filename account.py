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

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("balance.txt", 1)

checking.transfer(1000)
checking.commit()
print(checking.balance)
