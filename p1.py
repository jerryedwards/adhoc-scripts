for i in range(1,100):
    num = i + 1

    if num%3 == 0 and num%5 == 0:
       print(str(num) + ' is divisible by both 3 and 5')

    elif num%3 == 0:
       print(str(num) + ' divisible by only 3')

       breakpoint()

    elif num%5 == 0 and num%5 == 0:
       print(str(num) + ' divisible by only 5')

    else:
        print(num)