def solve(numheads, numlegs):
    chicks = 0
    rabbits = 0
    for i in range (1, numheads + 1):
        chicks = i
        rabbits = numheads - i
        if chicks*2 + rabbits*4 == numlegs:
            return rabbits, chicks
print(solve(35, 94))