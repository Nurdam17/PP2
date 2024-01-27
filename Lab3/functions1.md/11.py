def isPalindrome(word):
    # if word[::-1]==word:
    #     return True
    # else:
    #     return False
    return word[::-1]==word
word=input()
print(isPalindrome(word))