import logging as lg
lg.basicConfig(filename='assignment.log', level=lg.INFO ,format="%(levelname)s %(asctime)s %(message)s" )

# Q1. Write a Python program to Extract Unique dictionary values?

dic1 = {1:'himz', 2:'sudhanshu' , 3:'sunny', 4:'ineuron' , 5:'ineuron', 6:10, 7:10}
lg.info(f"Our dictionary: {dic1}")
l1,l2 = [],[]
for i,j in dic1.items():
    l1.append(j)
s = set(l1)
for i in s:
    if l1.count(i) == 1:
        l2.append(i)
lg.info(f"Unique values in dictionary: \n{l2}")


# Q2. Write a Python program to find the sum of all items in a dictionary?

dic2 = {'k1':10 , 'k2':'john cena', 'k3':20, 'k4':50}
lg.info(f"Now we will find sum of items in a dictionary:\n{dic2}")
item_sum = 0
l3 = []
for i,j in dic2.items():
    if type(j) == int:
        l3.append(j)
item_sum += sum(l3)
lg.info(f"Sum of all items in dictionary: {item_sum}")


# Q3. Write a Python program to Merging two Dictionaries?

d1 = {1:1, 2:2, 3:3}
d2 = {4:4, 5:5, 6:6}
lg.info(f"Now we will merge {d1} and {d2} into single dictionary")
d3 = {**d1, **d2}
lg.info(f"New Merged Dictionary {d3}")


# Q4. Write a Python program to convert key-values list to flat dictionary?

dic3 = {1:['k1','k2','k3'], 2:['Delhi', 'LA', 'Dubai']}
lg.info(f"Converting key-values list of flat dictionary from dict-\n{dic3}")
dic4 = dict(zip(dic3[1],dic3[2]))
lg.info(f"Here's the new flat dictionary\n{dic4}")


# Q5. Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict

dic5 = {'ineuron':'sudh', 1:'city', 'Hitman':47}
ord_dict = OrderedDict(dic5)
lg.info(f"Your Ordered Dictionary: {ord_dict}")
lg.info("Taking new key & Value to insert at beginning.")
key = input("Enter key")
val = input("enter Value")
lg.info(f"Key-Value pair --> {key}:{val}")
ord_dict.update({key:val})
ord_dict.move_to_end(key,last =False)
lg.info(f"New orderedict -> {ord_dict}")


# Q6. Write a Python program to check order of character in string using OrderedDict()?

stng = "this is test statement"
check = 'ht'
dict1 = OrderedDict.fromkeys(stng)
lg.info(f"Our string-> {stng} \nPattern to check-> {check}")
check_len = 0
for key, value in dict1.items():
    if (key == check[check_len]):
        check_len +=  1
    if (check_len == (len(check))):
        lg.info("Yes it is!")
lg.info("No it's not")


# Q7. Write a Python program to sort Python Dictionaries by Key or Value?
lg.info("Sorting Dictionary by Key :")
dictionary = {'ineuron':12, 'sudh':5, 'himz':22, 'dubai':1}
dictionary1 = OrderedDict(sorted(dictionary.items()))
lg.info(f"Our original Dictionary:\n{dictionary}\n Sorted Dicitonary by Keys-\n{dictionary1}")



