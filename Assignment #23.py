# Q1. Create a function that takes a number as an argument and returns True or False depending on
#     whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

def is_symmetrical(num):
    return True if str(num) == str(num)[::-1] else False

res1 = is_symmetrical(1112111)
print(res1)


# Q2. Given a string of numbers separated by a comma and space, return the product of the numbers.

import math

def multiply_nums(st):
    return math.prod([int(i) for i in st.split(', ')])

res2 = multiply_nums("-1, 2, 3, 4")
print((res2))


# Q3. Create a function that squares every digit of a number.

def square_digits(n):
    return "".join([str(int(i)**2) for i in str(n)])

res3 = square_digits(2483)
print(res3)


# Q4. Create a function that sorts a list and removes all duplicate items from it.

def setify(l):
    return list(set(l))

res4 = setify([5,7,8,9,5,10,15,5,8])
print(res4)


# Q5. Create a function that returns the mean of all digits.

def mean(n):
    return sum([int(i) for i in str(n)]) // len(str(n))

res5 = mean(666)
print(res5)