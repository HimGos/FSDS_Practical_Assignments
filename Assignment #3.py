# Q1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

num = int(input("Enter a number: "))
if num < 0:
    print("Negative Number")
elif num == 0 :
    print("Zero")
else :
    print("Positive Number")


# Q2. Write a Python Program to Check if a Number is Odd or Even?

num = int(input("\nEnter a number to find Even or odd: "))
if num%2==0 :
    print("Even Number")
else :
    print("Odd Number")


# Q3. Write a Python Program to Check Leap Year?

import calendar
year = int(input("\nEnter a year to find if it's leap: "))
leap_check = calendar.isleap(year)
if leap_check:
    print("Yes {} is a leap year.".format(year))
else:
    print("Not a leap year")


# Q4. Write a Python Program to Check Prime Number?

num = int(input("\nEnter a number to check if it's Prime: "))
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print(num,"is Prime Number")

# Q5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

num = 10000
print("\n All Prime Numbers b/w 1-10k")
for i in range(2,10000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,"is Prime Number")