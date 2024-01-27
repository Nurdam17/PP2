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