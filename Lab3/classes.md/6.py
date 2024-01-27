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