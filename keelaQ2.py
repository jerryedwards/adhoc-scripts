nums = [1, 2, 3, 4]
dict = {}

for num in nums:

    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

for key in dict:
    if dict[key] > 1:
        print("greater than 1")
        x = True
        break
    else:
        x = False

print(dict)
print(x)