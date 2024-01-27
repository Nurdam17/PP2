from itertools import permutations
def permut(word):
    perms = permutations(word)
    for i in list(perms):
        print(i)
word = input()
permut(word)