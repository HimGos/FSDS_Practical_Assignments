import re
import logging as lg
lg.basicConfig(filename="assignment.log", level=lg.INFO, format="%(levelname)s %(asctime)s %(message)s")

# Q1. Write a Python program to find words which are greater than given length k?

lg.info("Finding words greater than given length k")
line1 = "Hello! this is a simple line having words of various length."
k = int(input("Enter a length to filter out words: "))
great_line = ' '.join([i for i in line1.split() if len(i) >=k])

lg.info(f"Original String: \n {line1}\nWords in string greater than {k} length:\n {great_line}")


# Q2. Write a Python program for removing i-th character from a string?

lg.info("Removing i-th character from a string")

line2 = "Hello! Give an index and I'll remove that character."
ch = int(input("Enter the index no.: "))
rem_str = line2.replace(line2[ch],'',1)

lg.info(f"Original String:\n {line2}\n New string after removing {ch}th element:\n {rem_str}")


# Q3. Write a Python program to split and join a string?

lg.info("Split & Join a string")

line3 = "Example of split and joining string"
spl_join = '-'.join(line3.split())

lg.info(f"Original String:\n {line3}\n New string split join operation:\n {spl_join}")


# Q4. Write a Python to check if a given string is binary string or not?

lg.info("Program to check if string is binary")
line4 = input("Enter a binary string: ")
for i in set(line4):
    if i!='1' and i!='0' :
        lg.info(f"{line4} is not a binary string")
        break
else :
    lg.info(f"{line4} is a binary string")


# Q5. Write a Python program to find uncommon words from two Strings?

lg.info("Finding uncommon words from 2 strings")
st1 = "iNeuron is best in DS"
st2 = "NASA is best in space"
uncommon = set(st1.split()).symmetric_difference(set(st2.split()))

lg.info(f"First string ->{st1}\nSecond string ->{st2}\nUncommon words->{uncommon}")


# Q6. Write a Python to find all duplicate characters in string?

lg.info("Finding Duplicate characters in string")
st3 = "ineuron data science"
dic = {}
dup_lst = []
for i in st3:
    if i in dic: dic[i] += 1
    else : dic[i] = 1
for i,j in dic.items():
    if j>1 and i!=' ':
        dup_lst.append(i)

lg.info(f"In String: {st3}\nDuplicate characters are: {dup_lst}")



# Q7. Write a Python Program to check if a string contains any special character?

lg.info("Checking if string contains any special character.")
st4 = "A boy! He 'whispered': 1+1=& yes?'"
re_obj = re.findall(r'[^\w]',st4)
lg.info(f"Original String: {st4}\nSpecial Characters in it->{''.join(re_obj)}")




