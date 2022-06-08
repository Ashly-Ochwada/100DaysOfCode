def number(num):
    if num%2 == 0: #checking divisibility by 2
        if num > 10:
            print("Your number is even and greater than 10")
        else:
            print("Your number is even and smaller than or equal to 10")
    else:
        print("Your number is odd")

number(13)    