#Task1():
grams=float(input())
def grams_to_ounces(grams):
    print(grams * 28.3495231)
grams_to_ounces(grams)

#Task2():
fahrenheit_temperature=float(input())
def convertion(fahrenheit_temperature):
    print((5/9)*(fahrenheit_temperature-32))
convertion(fahrenheit_temperature)

#Task3():
def solve(numheads, numlegs):
    chicks = 0
    rabbits = 0
    for i in range (1, numheads + 1):
        chicks = i
        rabbits = numheads - i
        if chicks*2 + rabbits*4 == numlegs:
            return rabbits, chicks
print(solve(35, 94))

#Task4():
nums=[int(x) for x in input().split()]
new_array=[]
def filter_prime(nums):
    cnt_prime=0
    for i in range(len(nums)):
        if nums[i]==0 or nums[i]==1:
            continue
        else:
            for j in range(2, (nums[i]//2)+1):
                if nums[i]%j==0:
                    cnt_prime+=1
        if cnt_prime==0:
            new_array.append(nums[i])
        else:
            cnt_prime=0
filter_prime(nums)
print(new_array)

#Task5():
from itertools import permutations
def permut(word):
    perms = permutations(word)
    for i in list(perms):
        print(i)
word = input()
permut(word)

#Task6():
def rev(word):
    lst=word.split()
    print(lst[::-1])
word=input()
rev(word)

#Task7():
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    else:
        return False
    
print(has_33([3, 3, 1]))
print(has_33([1, 3, 1, 3]))
print(has_33([1, 3, 1]))

#Task8():
def spy_game(arr):
    return '0' and '0' and '7' in ''.join(str(i) for i in arr)

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#Task9():
def volume(r):
    v=4*3.14*(r**3)/3
    return v
r=int(input())
print(volume(r))

#Task10():
array = [int(x) for x in input().split()]
def unique(array):
    new_array = []
    for i in array:
        if i not in new_array:
            new_array.append(i)
    print(new_array)
unique(array)

#Task11():
def isPalindrome(word):
    # if word[::-1]==word:
    #     return True
    # else:
    #     return False
    return word[::-1]==word
word=input()
print(isPalindrome(word))

#Task12():
def histo(nums):
    for x in nums:
        print('*'*x)
    return
nums=[int(x) for x in input().split()]
histo(nums)

#Task13():
import random
print("Hello! What is your name?")
name=input()
print(name)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
guessed_number=random.randint(1, 20)
def guess(guessed_number):
    eq=False
    number_of_fails=1
    while eq==False:
        my_number=int(input())
        if my_number < guessed_number:
            print("Your guess is too low.")
            print("Take a guess")
            number_of_fails += 1
        elif my_number > guessed_number:
            print("Your guess is too high.")
            print("Take a guess")
            number_of_fails += 1
        else:
            eq=True
    print(f"Good job, {name}! You guessed my number in {number_of_fails} guesses!")
guess(guessed_number)