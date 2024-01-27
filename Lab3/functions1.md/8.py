def spy_game(arr):
    return '0' and '0' and '7' in ''.join(str(i) for i in arr)

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))