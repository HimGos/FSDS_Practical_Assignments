# Q1. Please write a program using generator to print the numbers which can be divisible by 5 and
#     7 between 0 and n in comma separated form while n is input by console.

def divi(x):
    for i in range(0,x):
        if i % 5 == 0 and i%7==0:
            yield i


lim = int(input("Till which numebr you want divisible of 5 and 7 -> "))
fiv_sev = [i for i in divi(lim)]
print(fiv_sev)



# Q2. Please write a program using generator to print the even numbers between 0 and n in comma
#     separated form while n is input by console.

def eves(x):
    for i in range(0,x):
        if i % 2 == 0:
            yield i


elim = int(input("Till which numebr you want even numbers -> "))
evens = [i for i in eves(elim)]
print(evens)



# Q3. Please write a program using list comprehension to print the Fibonacci Sequence in comma
#     separated form with a given n input by console.


def fib(n):
    f = []
    f.append(1)
    f.append(1)
    [f.append(f[i-1] + f[i-2]) for i in range(2, n)]
    return f

n = int(input("Till where you want to see fibonacci series! ->"))
res = fib(n)
print(res)



# Q4. Assuming that we have some email addresses in the "username@companyname.com" format,
#     please write program to print the user name of a given email address. Both user names and
#     company names are composed of letters only.

import re
email = input("Enter your email and I will fetch you username letters-> ")
ob = re.match(r'[a-zA-Z]+',email)
print(ob.group())



# Q5. Define a class named Shape and its subclass Square. The Square class has an init function
#     which takes a length as argument. Both classes have a area function which can print the area
#     of the shape where Shape's area is 0 by default.

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length**2

l = int(input("Enter the length of shape-> "))
shp = Shape()
sq = Square(l)
print("Area of shape - {}".format(shp.area()))
print("Area of sqaure- {}".format(sq.area()))