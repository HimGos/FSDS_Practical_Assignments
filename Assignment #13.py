import math
import re

# Q1. Square root of [(2 * C * D)/H]
#     Following are the fixed values of C and H:
#     C is 50. H is 30.
#     D is the variable whose values should be input to your program in a comma-separated sequence.


C = 50
H = 30
ele = int(input("How many numbers you wish in a list? -> "))
l,res = [],[]
for i in range(ele):
    l.append(int(input("Enter next numbers: ")))
for i in l:
    res.append(math.floor(math.sqrt((2*C*i)/H)))
print(res)


# Q2. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
#     element value in the i-th row and j-th column of the array should be i*j.
#     Note: i=0,1.., X-1; j=0,1,¡Y-1.

X = int(input("How many rows in array? "))
Y = int(input("How many columns in array? "))

print([[i*j for j in range(Y)] for i in range(X)])



# Q3. Write a program that accepts a comma separated sequence of words as input and prints the
#      words in a comma-separated sequence after sorting them alphabetically.

word_ele = int(input("How many words you wish in a list? -> "))
word_input = []
for i in range(word_ele):
    word_input.append(input("Enter your word: "))
sort_word = sorted(word_input)
print(sort_word)


# Q4. Write a program that accepts a sequence of whitespace separated words as input and prints
#      the words after removing all duplicate words and sorting them alphanumerically.

sentnc = input("Enter your sentence here: ")
sen_list = sentnc.split()
sort_unique = ' '.join(sorted(list(set(sen_list))))
print(sort_unique)


# Q5. Write a program that accepts a sentence and calculate the number of letters and digits.

sen = input("Enter your sentence having words and digits: ")
dig_num = len(re.findall('[0-9]',sen))
let_num = len(re.findall('[a-zA-Z]',sen))
print(f"DIGITS: {dig_num}\nLETTERS: {let_num}")


# Q6. A website requires the users to input username and password to register. Write a program to
#     check the validity of password input by users.
#     Following are the criteria for checking the password:
#       1. At least 1 letter between [a-z]
#       2. At least 1 number between [0-9]
#       3. At least 1 letter between [A-Z]
#       4. At least 1 character from [$#@]
#       5. Minimum length of transaction password: 6
#       6. Maximum length of transaction password: 12

psw = 'ABd1234@1, aF1#, 2w3E* , 2We3345, zXd1234@1'
pswrd = re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@!%&*?])[A-Za-z\d#$@!%&*?]{6,12}',psw)
print(pswrd)

