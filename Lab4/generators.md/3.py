n = int(input())
def div(n):
    for x in range(n+1):
        if x%3==0 and x%4==0:
            yield x
for y in div(n):
    print(y)