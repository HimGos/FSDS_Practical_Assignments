# Q1. Find LCM
import math
def lcm(a,b):
    if a <= 0 or b<=0:
        print("Please enter a number greater than 0")
    else:
        return math.lcm(a,b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = lcm(a,b)
print("LCM is: ",result)


# Q2. Find HCF
def hcf(a,b):
    if a <= 0 or b <= 0:
        print("Please enter a number greater than 0")
    else:
        if a>b:
            small = b
        else:
            small = a
        for i in range(1,small+1):
            if a%i==0 and b%i==0:
                prod = i
        return prod
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
result = hcf(a,b)
print("HCF is: ",result)


# Q3. Convert Decimal to Binary, Octal and Hexadecimal?

def conv(n):
    if type(n) == int:
        binary = bin(n)
        octal = oct(n)
        hexa = hex(n)
    return "Binary - {} , Octal - {} , Hexadecimal - {} ".format(binary,octal,hexa)

num = int(input("Enter a number to find it's binary, octal and hexadecimal -> "))
result = conv(num)
print(result)


# Q4. Write a Python Program To Find ASCII value of a character?

def asc(ch):
    return ord(ch)

ch = input("Enter any character to find it's ascii : ")
result = asc(ch)
print(result)


# Q5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def cal(a, b):
    while True:
        option = int(input("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide\nPick any one of them: "))
        if option <= 4 and option >= 1:
            if option == 1:
                return a + b
                break
            elif option == 2:
                return a - b
                break
            elif option == 3:
                return a * b
                break
            else:
                return a / b
                break
        else:
            print("Enter between 1-4!")
            continue


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = cal(num1, num2)
print(result)