n = int(input())
def even(n):
    for x in range(n+1):
        if x%2==0:
            yield x
for y in even(n):
    print(y, end = ' ')