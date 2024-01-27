a = int(input())
b = int(input())
def square(a, b):
    for x in range(a, b+1):
        yield x**2

for y in square(a, b):
    print(y)