# Q1. Create a function that takes three integer arguments (a, b, c) and returns the amount of
#       integers which are of equal value.

def equal(a,b,c):
    return [3 if a==b==c else 2 if a==b or b==c or c==a else 0]

res1 = equal(3,4,3)
print(res1[0])


# Q2. Write a function that converts a dictionary into a list of keys-values tuples.

def dict_to_list(d):
    return sorted([i for i in d.items()])

res2 = dict_to_list({"D":1, "B":2, "C":3})
print(res2)


# Q3. Write a function that creates a dictionary with each (key, value) pair being the (lower case,
#     upper case) versions of a letter, respectively.

def mapping(l):
    return dict(zip(l,map(lambda i:i.upper(), l)))

res3 = mapping(['a','v','y','z'])
print(res3)


# Q4. Write a function, that replaces all vowels in a string with a specified vowel.

import re
def vow_replace(st,v):
    return re.sub('[aAeEiIoOuU]',v,st)

res4 = vow_replace("Apples and bananas", 'u')
print(res4)


# Q5. Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
#     and returns its lower case version if its ASCII code is odd.

def ascii_capitalize(st):
    return "".join([i.upper() if ord(i)%2==0 else i.lower() for i in st])

res5 = ascii_capitalize("Oh what a beautiful morning.")
print(res5)