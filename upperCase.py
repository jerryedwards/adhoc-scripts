# Write a function named capital_indexes. The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(s):
    upperCaseList = []
    i = 0
    
    for letter in s:
        if letter.isupper() == True:
            upperCaseList.append(i)
        
        i += 1
    
    return upperCaseList
    
list = capital_indexes("HeLlO")
print(list)