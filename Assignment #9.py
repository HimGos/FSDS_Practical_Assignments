# Q1. Write a Python program to check if the given number is a Disarium Number?

import logging
logging.basicConfig(filename="assignment.log", level = logging.INFO, format=r"%(levelname)s %(asctime)s %(message)s")
logging.info("Start of Disarium check program.")

num = int(input("Enter a number to find if it's Disarium: "))
logging.info(f"Entered number {num}")

l = len(str(num))
count = 0

for i in range(0,l):
    count += int(str(num)[i])**(i+1)
if count == num:
    logging.info(f"Yes {num} is Disarium")
else :
    logging.info("No it's not Disarium")

logging.info("End of first question")


# Q2. Write a Python program to print all disarium numbers between 1 to 100?

logging.info("Now we print all disarium numbers between 1-100")

for i in range(1,101):
    len_num = len(str(i))
    count = 0
    for j in range(0,len_num):
        count += int(str(i)[j])**(j+1)
    if count == i:
        logging.info(f"{i} is Disarium")

logging.info("End of second Question")


# Q3. Write a Python program to check if the given number is Happy Number?

logging.info("Now we will check if number is Happy! :)")

hap_check = int(input("Enter a number to check if it's happy: "))
logging.info(f"Entered number is {hap_check}")


rep = set()
while hap_check != 1:
    len_hap = len(str(hap_check))
    hap_check = sum(int(i)**2 for i in str(hap_check))
    if hap_check in rep:
        logging.info("Not a Happy Number")
        break
    elif hap_check == 1:
        logging.info("Yes it's a Happy Number")
        break
    rep.add(hap_check)


# Q4. Write a Python program to print all happy numbers between 1 and 100?

logging.info("Now we will check happy numbers from 1-100")

for i in range(1,101):
    temp = i
    repeat = set()
    while i != 1:
        len_i = len(str(i))
        i = sum(int(j)**2 for j in str(i))
        if i in repeat:
            break
        elif i == 1:
            logging.info(f"{temp} is a Happy number")
        repeat.add(i)
logging.info("End of Question 4")



# Q5. Write a Python program to determine whether the given number is a Harshad Number?

logging.info("Now we will check if a number is Harshad")

n = int(input("Enter a number to check if it's harshad: "))
len_n = len(str(n))
sum_digits = sum(int(i) for i in str(n))

logging.info(f"Sum of digits of {n} is {sum_digits}")
if n % sum_digits == 0:
    logging.info(f"Yes {n} is Harshad Number")
else :
    logging.info("Not a harshad number")

logging.info("End of Question 5")


# Q6. Write a Python program to print all pronic numbers between 1 and 100?
import math
logging.info("Now we will print all pronic numbers between 1-100")

for i in range(1,101):
    k = math.floor(i**0.5)
    if k*(k+1) == i :
        logging.info(f"{i} is Pronic Number")




# Thank you Sudhanshu Sir, I am feeling very confident in coding after solving these assignments. God Bless You Always :)
