class account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def print_balance(self):
        print(self.balance)

    def print_owner(self):
        print(self.owner)
    
    def deposit(self, money):
        self.balance += money
        print("Deposit accepted.")

    def withdrawal(self, money):
        if self.balance >= money:
            self.balance -= money
            print("Withdrawal accepted.")
        else:
            print("Unavailable.")
acc1 = account(input(), int(input()))
acc1.deposit(int(input())) #to give money to bank account
acc1.withdrawal(int(input())) #to get money from bank account
acc1.print_balance() #to see current balance
acc1.print_owner() #to see owner name