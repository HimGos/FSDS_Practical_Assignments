# Q1. Write a Python program to convert kilometers to miles?
km = float(input("How much km you wanna convert to miles: "))
mil = km*0.621371
print("Miles: ", mil)


# Q2. Write a Python program to convert Celsius to Fahrenheit?
cel = float(input("How much celcius to convert to Fahrenheit: "))
fah = (cel*1.8)+32
print("Fahrenheit: ", fah)


# Q3. Write a Python program to display calendar?

import calendar
year = int(input("Enter a year to print calender of: "))
cal = calendar.calendar(year)
print(cal)


# Q4. Write a Python program to solve quadratic equation?

import math
while True:
    a = int(input("Enter value of a except 0: "))
    if a != 0 :
        break
    else:
        print("Enter valid number")
        continue
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))

disc = (b**2 - 4*a*c)
val_sq = math.sqrt(abs(disc))

if disc == 0 :
    print("The Quadratic Equation will have equal roots")
    equal_root = (-b / (2*a))
    print("Since discriminant is equal to zero, root is : {}".format(equal_root))

elif disc < 0 :
    print("Equation will have 2 imaginary roots")
    real_part = (-b/(2*a))
    img_part1 = -(val_sq/(2*a))
    img_part2 = (val_sq/(2*a))
    print("2 Imaginary roots are : {}+{}i  and {}{}i".format(real_part,img_part2,real_part,img_part1))

else :
    print("Equation will have 2 real roots.")
    root1 = ((-b + val_sq) / (2*a))
    root2 = ((-b - val_sq) / (2*a))
    print("2 roots are: {}  and  {}".format(root1,root2))



# Q5. Write a Python program to swap two variables without temp variable?

a = 11
b = 19
print("Old values of a and b are : {} and {}".format(a,b))
a,b = b,a
print("New Values of a and b are : {} and {}".format(a,b))