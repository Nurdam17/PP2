n = int(input())
def reverse(n):
    for x in range(n, -1, -1):
        yield x
for y in reverse(n):
    print(y)