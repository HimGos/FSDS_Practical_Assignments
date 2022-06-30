# Q1. Write a Python Program to Add Two Matrices?

import numpy as np

mat1 = np.arange(9,18).reshape(3,3)
mat2 = np.ones((3,3),dtype=int)

print(f"Matrices are\n {mat1} \nand \n{mat2}")
print("Addition : \n", mat1+mat2)


# Q2. Write a Python Program to Multiply Two Matrices?

mat3 = np.linspace(5,25,num=9,dtype=int).reshape(3,3)
mat4 = np.arange(2,11).reshape(3,3)

print(f"Matrices are\n {mat3} \nand \n{mat4}")
print("Multiplication : \n", mat3@mat4)


# Q3. Write a Python Program to Transpose a Matrix?

mat5 = np.linspace(1,17,num=6,dtype=int).reshape(2,3)
mat6 = np.transpose(mat5)
print(f"Original Matrix:\n{mat5}")
print(f"\nTransposed Matrix:\n{mat6}")


# Q4. Write a Python Program to Sort Words in Alphabetic Order?

line = "This is just an enhanced testing phrase to sort all the quizes in alphabetical order."
newline = ' '.join(sorted((line.lower()).split()))
print(f"\nOriginal string:\n{line} \n New string: \n{newline}")


# Q5. Write a Python Program to Remove Punctuation From a String?

import re
string = """Hello, this is a "secret" message! My intel-five team has sent:('Coding.is.easy?']"""
res = re.sub(r'[^\w\s]', '', string)
print(f"\nOriginal String:\n{string}\n New String Without punctuation:\n{res}")