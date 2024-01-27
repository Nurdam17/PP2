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