#Task1():
class string():
    def __init__(self):
        self.str=""
    def getString(self):
        self.str=input()
    def printString(self):
        print(self.str.upper())

str=string()
str.getString()
str.printString()

#Task2():
class shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class square(shape):
    def __init__(self, l):
        shape.__init__(self)
        self.length = l
    def area(self):
        return self.length * self.length
sq = square(int(input()))
print(sq.area())

#Task3():
class rectangle():
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

a = int(input())
b = int(input())
r = rectangle(a, b)
print(r.area())

#Task4():
import math
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y
    
    def move(self, a, b):
        return self.x + a, self.y + b
    
    def dist(self, c, d):
        dx = self.x - c
        dy = self.y - d
        s = (dx**2 + dy**2)
        return s**0.5
    
x = int(input())
y = int(input())
p = point(x, y)
print(p.show())
print(p.move(int(input()), int(input())))
print(p.dist(int(input()), int(input())))

#Task5():
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

#Task6():
lst = [int(x) for x in input().split()]
def isPrime(num):
    if num==0 or num==1:
        return 0
    if num>1:
        for x in range(2, int(num**0.5)+1):
            if num%x==0:
                return 0
        return 1
new_list = list(filter(lambda x : (isPrime(x)==1), lst))
print(new_list)