array = [int(x) for x in input().split()]
def unique(array):
    new_array = []
    for i in array:
        if i not in new_array:
            new_array.append(i)
    print(new_array)
unique(array)