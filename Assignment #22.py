# Q1. Return an ordered list with numbers in the range that are divisible by the third parameter n.
#     Return an empty list if there are no numbers that are divisible by n.

def list_operation(x,y,n):

    return [i for i in range(x,y+1) if i%n == 0]

res1 = list_operation(1,10,3)
print(res1)


# Q2. Create a function that takes in two lists and returns True if the second list follows the first list
#     by one element, and False otherwise. In other words, determine if the second list is the first
#     list shifted to the right by 1.

def simon_says(l1,l2):
    if len(l1) == len(l2) and len(l1) >2:
        if l1[:-1] == l2[1:] :
            return True
        else :
            return False
    else:
        return "invalid lists"


res2 = simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
print(res2)


# Q3. Create a function that takes in a list of names and returns the name of the secret society.

def society_name(lst) :
    return "".join([i[0] for i in lst])

res3 = society_name(["Adam",'Eve','Charlene'])
print(res3)


# Q4. An isogram is a word that has no duplicate letters. Create a function that takes a string and
#     returns either True or False depending on whether or not its an "isogram".

def is_isogram(st):
    if sorted(st.lower()) == sorted(set(st.lower())):
        return True
    else :
        return False

res4 = is_isogram("PasSword")
print(res4)


# Q5. Create a function that takes a string and returns True or False, depending on whether the
#     characters are in order or not.

def is_in_order(st):
    if "".join(sorted(st.lower())) == st.lower():
        return True
    else :
        return False

res5 = is_in_order("xyzz")
print(res5)