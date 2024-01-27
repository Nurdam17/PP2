n = int(input())
def square(n):
    for x in range(n+1):
        if x**2>n:
            break
        yield x**2

for y in square(n):
    print(y)