#Write a function for checking the speed of drivers. This function should have one parameter: speed.
#If speed is less than 70, it should print “Ok”.
#Otherwise, for every 5km above the speed limit (70), it should give the driver 
# one demerit point and print the total number of demerit points. For example, 
# if the speed is 80, it should print: “Points: 2”.
#If the driver gets more than 12 points, the function should print: “License suspended”

def speed_check(speed):
    speedlimit=70
    dermitpoint=(speed-speedlimit*1)//5
    if speed<70:
        print("okay")
    elif dermitpoint>12 and speed>70:
        print("lisence suspended")
    elif speed>70:
        print(f"Points:{dermitpoint}")
    else:
        print("none")
speed_check(310)


#Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the 
# even and odd numbers      
# def numbers(limit):
#     for i in (0,range+1):
#         if i%2==0:
#             print(f"{i} is an even number")
#         else:
#             print(f"{i} is an odd number")    
   




#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.



#Write a function called show_stars(rows). If rows is 5, it should print the following:
#*
# **
# ***
# ****
# *****



#Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
