# Q1. Write a Python program to print "Hello Python"?
print("Hello Python")

# Q2. Write a Python program to do arithmetical operations addition and division.?
a,b = 15,10
print("Addition: {}  and Division: {} ".format((a+b),(a/b)))

# Q3. Write a Python program to find the area of a triangle?
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = 1/2 * (base * height)
print("Area Of Triangle: ",area)

# Q4. Write a Python program to swap two variables?
a = 11
b = 12
a,b = b,a
print('New value of a: {} , New value of b: {}'.format(a,b))

# Q5. Write a Python program to generate a random number?

import random
start,till = int(input("From where you want random number: ")) , int(input("Till which number: "))
num = random.randrange(start,till)
print(num)