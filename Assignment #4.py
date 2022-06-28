# Q1. Write a Python Program to Find the Factorial of a Number?

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))     # Using Recursion

find_fac = fact(5)
print(find_fac)


# Q2. Write a Python Program to Display the multiplication Table?

num = int(input("\nEnter a number to see it's multiplication table: "))
for i in range(1,11):
    print("{} X {} is = {}".format(num,i,num*i))


# Q3. Write a Python Program to Print the Fibonacci sequence?

num = int(input("\nHow many fibonacci series you wanna see? "))
a,b = 1,1
fib_lst = []
for i in range(1,num):
    fib_lst.append(a)
    a,b = b,b+a
print(fib_lst)


# Q4. Write a Python Program to Check Armstrong Number?

n = int(input("\nEnter a number to check if its armstrong: "))
ln = len(str(n))
count = 0
for i in str(n):
    count += int(i)**ln
if count == n:
    print(n,"is an Armstrong Number")
else:
    print("Not an armstrong number")


# Q5. Write a Python Program to Find Armstrong Number in an Interval?

print("\nSince 153 is the lowest armstrong number, we will start count from 150 to save power & time")
mn = 150
mx = 3000
for i in range(mn,mx+1):
    ln = len(str(i))
    count = 0
    for j in str(i):
        count += int(j)**ln
    if count==i:
        print(i,"Armstrong Number")


# Q6. Write a Python Program to Find the Sum of Natural Numbers?

limit = int(input("\nHow many natural numbers you wanna add: "))
count = 0
for i in range(1,limit+1):
    count += i
print(count)
