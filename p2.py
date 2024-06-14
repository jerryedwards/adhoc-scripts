# -----------------------------
# Problem 1: print numbers 1-10

#i = 1
#
#while i < 11:
#    print(i)
#    i += 1

# -----------------------------
# Problem 2: print triangular numbers pattern

j = 1
nums = []

while j < 6:
    nums.append(j)
    #print('nums is: ' + str(nums))

    numsStr = ''

    for num in nums:
        numsStr = numsStr + str(num)
        #print('numStr is: ' + str(numsStr))
    
    print(numsStr)
    j += 1


# -----------------------------
# Problem 3: Calculate the sum of all numbers from 1 to a given number

endNum = input("Enter the numer to sum to: ")

i = 1
sum = 0

while i <= int(endNum):
    sum += i
    i += 1

print('Sum of all numbers up to {} is {}'.format(endNum, sum))


# -----------------------------
# Problem 4: Write a program to print multiplication table of a given number

num = input("Enter a number for a multiplication table: ")

for i in range(1, 11, 1):
    print(i*int(num))


# -----------------------------
# Problem 5: Display numbers from a list using loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

print("starting problem 5...10")

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 150:
        continue

    if num > 500:
        break

    if num % 5 == 0:
        print(num)