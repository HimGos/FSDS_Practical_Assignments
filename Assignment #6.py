# Q1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fib(n):
    if n <=1:
        return 1
    else :
        return (fib(n-1) + fib(n-2))

series = int(input("How many fibo series? ->"))

for i in range(series):
    print(fib(i))


# Q2. Write a Python Program to Find Factorial of Number Using Recursion?

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

num = int(input("\nEnter a number to see it's factorial: "))
result = fac(num)
print(result)


# Q3. Write a Python Program to calculate your Body Mass Index?

def bmi(wght,hght):
    return wght/(hght/100)**2

wt = float(input("\n Welcome to BMI Calc.\n Enter your weight in KG: "))
ht = float(input("\nEnter Your height in cm: "))
bmi_result = bmi(wt,ht)
print("Your BMI:",bmi_result)


# Q4. Write a Python Program to calculate the natural logarithm of any number?

import math
def log_val(n):
    return math.log(n)

num = int(input("\nenter a number to see it's log value: "))
logres = log_val(num)
print(logres)


# Q5. Write a Python Program for cube sum of first n natural numbers?

def nat(n):
    return ((n**2)*((n+1)**2))/4

num = int(input("\nHow many first natural numbers you see cube sum of: "))
nat_res = nat(num)
print(nat_res)