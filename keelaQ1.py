import random

def random5():
    return random.randint(0, 5)

def random8():
    n = random5()
    m = random.randint(0, 3)
    return n + m

    # first solution
    # m = abs(random5() - 2)
    # return n + m

dict = {}

for i in range(1000):

    randomNum = random8()
    
    if randomNum in dict:
        dict[randomNum] += 1
    else: 
        dict[randomNum] = 1

print(sorted(dict.items()))


'''
possibilites for first solution:

n = 1, 2, 3, 4, 5
m = 1, 0, 1, 2, 3

n + m

'''


