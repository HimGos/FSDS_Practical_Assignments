# Q1. Create a function that takes three arguments a, b, c and returns the sum of the
#     numbers that are evenly divided by c from the range a, b inclusive.

def three(a,b,c):
    if b>c:
        return sum(i for i in range(c,b+1,c))
    else:
        return 0

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter divisible number: "))
print(three(a,b,c))



# Q2. Create a function that returns True if a given inequality expression is correct and False otherwise.

def ineq():
    a = eval(input("Enter inequality expression: "))
    return a

print(ineq())



# Q3. Create a function that replaces all the vowels in a string with a specified character.

import re

st1 = input("Enter your string: ")
spc = input("Enter your special character to replace with vowels in your string: ")
replace_vowel = re.sub(r'[AaEeIiOoUu]+',spc,st1)
print(replace_vowel)



# Q4. Write a function that calculates the factorial of a number recursively.

def fact(num):
    if num == 1:
        return 1
    else :
        return num*fact(num-1)

n = int(input("Enter a number to find it's factorial: "))
print(fact(n))



# Q5. Create a function that computes the hamming distance between two strings.

def ham(s1,s2):
    a = sorted(s1)
    b = sorted(s2)
    for i in range(len(a)):
        if a[i] not in b:
            c = ord(a[i])
        if b[i] not in a:
            d = ord(b[i])
    return abs(c - d)

s1 = input("First string: ")
s2 = input("Second string: ")
print(ham(s1,s2))