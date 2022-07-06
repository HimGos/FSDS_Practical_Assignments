# Q1. Define a class with a generator which can iterate the numbers, which are divisible by 7,
#     between a given range 0 and n.

class Seven:
    def div(self,x):
        for i in range(x):
            if i % 7 == 0:
                yield i


lim = int(input("Enter a range till where you want 7 divisibles: "))
seven_obj = Seven()
for i in seven_obj.div(lim):
    print(i)



# Q2. Write a program to compute the frequency of the words from the input. The output
#     should output after sorting the key alphanumerically.

from collections import Counter
st = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
st_spl = sorted(st.split())
a = Counter(st_spl)
for i,j in a.items():
    print(i,':',j)



# Q3. Define a class Person and its two child classes: Male and Female. All classes have a
#     method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    def getGender(self):
        print("Check")

class Male(Person):
    def getGender(self):
        print("male")

class Female(Person):
    def getGender(self):
        print("female")

boy = Male()
girl = Female()
human = Person()

a = boy.getGender()
b = girl.getGender()



# Q4. Please write a program to generate all sentences where subject is in ["I, "You"] and
#     verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

from itertools import product

def sent(*args):
    com = product(*args)
    for i in com:
        yield i


com_sent = sent(["I", "You"],["Play", "Love"],["Hockey", "Football"])
for i in com_sent:
    print(' '.join(i))



# Q5. Please write a program to compress and decompress the string
#     "hello world!hello world!hello world!hello world".

import re
string = "hello world!hello world!hello world!hello world"
reg_exp = re.compile(r'hello world!')
comp_string = reg_exp.search(string).group()
print(f"Compressed string: {comp_string}")
print(f"Decompressed String: {comp_string*4}")



# Q6. Please write a binary search function which searches an item in a sorted list. The
#     function should return the index of element to be searched in the list.

lst = [12,23,34,45,56,67,78,81,97,100,132,156,180,230,275,310,320]
search = int(input(f"Enter your search no. in list {lst}-> "))

initial = lst[0]
mid = len(lst)//2
end = lst[len(lst)-1]
while True:
    for i in range (initial, end):
        if search == lst[mid]:
            print(f"Found {search} at index {mid}")
            break
        else :
            if search > lst[mid]:
                initial = lst[mid]
                mid = (lst.index(initial)+lst.index(end))//2
            else :
                end = lst[mid]
                mid = (lst.index(initial)+lst.index(end))//2
    break