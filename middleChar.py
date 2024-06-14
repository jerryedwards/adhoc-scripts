import math

def mid(s):
    numChars = len(s)
    middleNum = float()

    if not numChars % 2 == 0:
        middleNum = math.ceil(numChars / 2)
        print("numChars: {}\nmiddleNum: {}".format(numChars, middleNum))
        return s[middleNum-1]
    else:
        return ""
    
middleChar = mid("abcde")
print(middleChar)

