class string():
    def __inti__(self):
        self.str=""
    def getString(self):
        self.str=input()
    def printString(self):
        print(self.str.upper())

str=string()
str.getString()
str.printString()