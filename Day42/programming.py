import math
#Exercise 1: Write a program in Python to calculate the volume of a sphere.
def sphere_area(r):
    A = 4/3*math.pi*r**3
    return A
print(sphere_area(2))    
#Exercise 2: Write a program in Python to display a below-given pattern.
a = int(input("Enter number: "))
for b in range(a):
    for i in range (b):
        print(b, end=' ')
    print("\a")    
#Exercise 3: Range function program to return multiple of 7 within a given range 1,30.
num = range(1,30)
for i in num:
    if i%7==0:
        print(i)
#Exercise 4: Write a program in Python to swap between two numbers without using a third variable.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"\na is {a} b is {b}")
a = a + b
b = a - b
a = a - b
print("\nafter swapping")
print(f"a is {a} b is {b}")

#Exercise 5: Write a program to check wheteher the given word is vowel or consonent.
vowel = input("Enter alphabet: ")
if vowel in ["a","e","i","o","u"]:
    print("Is vowel")
else:
    print("Is a consonent")    
#Exercise 7: Write a program to count the occurence of even number and odd number between the range 10 – 55.
even_num = 0
odd_num=0
for w in range (10,56):
    if w%2==0:
        even_num+1
    else:
        odd_num+1
print(f"Even numbers are {even_num}")
print(f"Odd numbers are {odd_num}")            
        
#Exercise 8: Write a program to perform subtract and addition operation using switch.


#Exercise 9: Write a program in Python to calculates acceleration given initial velocity v1, 
# final velocity v2, start time t1, and end time t2
def acceleration(v1,v2,t1,t2):
    a = (v2 - v1 / t2 - t1)
    print(a)
acceleration(0,10,0,20) 
#Exercise 10: Write a program in Python to sort 3 numbers without 
# using loops or conditional statements.   
var1 = 2
var2 = 3
var3 = 4
list = [var1,var2,var3]
list.reverse()
print()
#Exercise 11: Write a program in Python to print number 
# ranging from 1 to 25 but excluding number which is the multiples of 5.
def number():
    x = range(1,25)
    for i in x:
        if i%5!=0:
            print(i)
number() 
#Exercise 12: Write a program in Python to count the occurrence of a specific value in a list.
def occurence():
    number = [1,2,4,5,4,6,7,4,9,4,7]
    num=number.count(4)
    print(num)
occurence()    
        
#Exercise 13: Write a program in Python to count the occurrence of a specific word in a string.
def word_occurence():
    words = ["Ashly", "Ochwada","Ashly","Noellah","Walala"] 
    word = words.count("Ashly")
    print(word)       
word_occurence()
#Exercise 14: Write a  program in Python to check whether the given number is even or odd.
def check_even():
    nums = int(input("Enter number: ")) 
    if nums%2==0:
        print(f"{nums} is Even")
    else:
        print(f"{nums} is Odd")      
check_even()        
#Exercise 15: Given two integer numbers return their product. 
# If the product is greater than 500, then return their sum.
def  integer_nums():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    product = a*b
    sum = a+b
    if product >500:
        print(product)
    else:
        print(sum)    

#Exercise 16: Write a program to print the greatest of three number.
def max_num():
    m_num = [5,6,7]
    w = max(m_num)
    print(w)
max_num()    

#Exercise 17: Write a program to print all numbers multiple of 5 from the range 10 – 50. 
def multiple_of_five():
    mul_num = range(10,50)
    for l in mul_num:
        if l%5!=0:
            pass
        else:
            print(l)
multiple_of_five()            

#Exercise 18: Write a program to check, the first and last elements of the list is same or not. 
# If same print True else False. 
def elements():
    b = [2,3,4,5,6,7,2]
    if b[0] == b[-1]:
        print("True")
    else:
        print("False")
elements()
#Exercise 19: Write a program to convert, the Fahrenheit value to Celcius. 
# [Formula : F=9/5(c)+32] 
def fahcel(f):
    celcius = (f-32)*5/9
    print(celcius)
fahcel(30)    
 
#Exercise 20: Write a program to print a right angled triangle pattern
def triangle():
    for i in range (triangle):
        for j in range (i):
            print("*", end='')
triangle(6)            

