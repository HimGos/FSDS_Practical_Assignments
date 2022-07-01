import logging as lg
import numpy
lg.basicConfig(filename='assignment.log', level=lg.INFO, format="%(levelname)s %(asctime)s %(message)s")

# Q1. Write a Python program to find sum of elements in list?

lg.info("This program find sum of elements in list")
lst1 = [1,2,3,4,5,6,7,8]

lg.info(f"List to operate on: {lst1}")
sum_elem = sum(i for i in lst1 if type(i)==int)
lg.info(f"sum of list elements: {sum_elem}")


# Q2. Write a Python program to Multiply all numbers in the list?

lg.info("This program will multiply all numbers in the list")

lst2 = [2,3,4,5,10]
lg.info(f"Now we will multiple elements of list: {lst2}")
mul_elem = numpy.prod(lst2)
lg.info(f"Product of list : {mul_elem}")


# Q3. Write a Python program to find smallest number in a list?

lg.info("This program will find smallest number in list")

lst3 = [12,34,45,32,10,987,213,2,19]
lg.info(f"Finding smallest element out of {lst3}")
smal_elem = numpy.min(lst3)
lg.info(f"Minimum value: {smal_elem}")


# Q4. Write a Python program to find largest number in a list?

lg.info("This program will find largest number in list")

lst4 = [12,34,45,32,11,987,213,2,19]
lg.info(f"Finding largest element out of {lst4}")
lar_elem = numpy.max(lst4)
lg.info(f"Minimum value: {lar_elem}")


# Q5. Write a Python program to find second largest number in a list?

lg.info("This program will find Second largest number in list")

lst5 = [12,34,45,32,11,987,213,2,19]
lg.info(f"Finding second largest in {lst5}")
lar2_elem = numpy.sort(lst5)[-2]
lg.info(f"Second largest {lar2_elem}")


# Q6. Write a Python program to find N largest elements from a list?

lg.info("This program will find N largest number in list")
lst6 = [12,34,45,32,11,987,213,2,19]

while True:
    try:
        N = int(input(f"How many largest elements you want out of list : {lst6} \n ->"))
        if N <= len(lst6):
            break
    except:
        print("input exceed the length of list! Try again")
        continue

lg.info(f"Finding {N} largest in {lst6}")

Nlar_elem = numpy.sort(lst6)[-N:]
lg.info(f"{N} largest elemenets {Nlar_elem}")


# Q7. Write a Python program to print even numbers in a list?

lg.info("Printing Even Numbers in list")
lst7 = [1,2,3,4,5,6,7,11,22,33,44]
lg.info(f"List from which we will find evens : {lst7}")
eve = [i for i in lst7 if i%2==0]

lg.info(f"Even number: {eve}")


# Q8. Write a Python program to print odd numbers in a list?

lg.info("Printing Odd Numbers in list")
lg.info(f"List from which we will find odds : {lst7}")
od = [i for i in lst7 if i%2!=0]

lg.info(f"Odd number: {od}")


# Q9. Write a Python program to Remove empty List from List?

lg.info("Removing Empty list from list")
lst9 = ['himz','sudh',2,[],5,[],67,'john cena',['not','empty'],1]
lg.info(f"List we are operating : {lst9}")

for i in lst9:
    if type(i) == list:
        if len(i) == 0 :
            lst9.pop(lst9.index(i))

lg.info(f"New List: {lst9}")


# Q10. Write a Python program to Cloning or Copying a list?

lg.info("Copying or cloning list")

org_list = ['himz', 'sudh', 1,2,3,4,(100,200),23.3]
lg.info(f"Original list: {org_list}")

clon_list = org_list[:]
lg.info(f"Clone List: {clon_list}")


# Q11. Write a Python program to Count occurrences of an element in a list?

lg.info("Now we will count occurences of elements in list")

lst11 = [12,12,'himz','himz',5,4,23,3,12,5,6,5,3,4]
lg.info(f"List we have: {lst11}")

rep = set(lst11)
for i in rep:
    count = 0
    count += lst11.count(i)
    lg.info(f"Total {i} : {count}")