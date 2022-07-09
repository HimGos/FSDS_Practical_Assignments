# Q1. Create a function that takes a list of non-negative integers and strings and
#     return a new list without the strings.

def nostr(l):
    return [i for i in l if type(i)==int]

print(nostr([1,2,3,'a','sudh','himz']))



# Q2. The "Reverser" takes a string as input and returns that string in reverse order,
#     with the opposite case.

def reverser(s):
    return s.swapcase()[::-1]

a = input("Enter a string to find it reversed with opposite case: ")
print(reverser(a))



# Q3. Your task is to unpack the list writeyourcodehere into three variables, being first,
#     middle, and last, with middle being everything in between the first and last element. Then
#     print all three variables.

def unpack(st):
    first = st[0]
    middle = st[1:-1]
    last = st[-1]
    return f'First element: {first}\nSecond element: {middle}\nThird element: {last}'

print(unpack('writeyourcodehere'))



# Q4. Write a function that calculates the factorial of a number recursively.

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

f = int(input("Enter a number to find it's factorial: "))
print(fact(f))



# Q5. Write a function that moves all elements of one type to the end of the list.

def move(lst,element):
    a = lst.count(element)
    for i in range(a):
        lst.remove(element)
        lst.append(element)
    return lst

lst = ['a','a','b','c',1,45,2]
print(move(lst,'a'))