# Q1. Create a function that takes a list of strings and integers, and filters out the list so that it
#     returns a list of integers only.

def filter_list(l):
    return [i for i in l if type(i)==int]

l = [1,2,3,4,'a','specific']
res = filter_list(l)
print(res)


# Q2. Given a list of numbers, create a function which returns the list but with each element's
#     index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
#     number at index 1, etc...

def add_indexes(l):
    return [l[i]+i for i in range(len(l))]

l1 = [1,2,3,4,5]
check = add_indexes(l1)
print(check)


# Q3. Create a function that takes the height and radius of a cone as arguments and returns the
#     volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

def cone_colume(h,r):
    return (3.14*(r**2)*h)/3

height = float(input("Enter the height of cone: "))
radius = float(input("Enter the radius of cone: "))
vol = cone_colume(height,radius)
print(vol)


# Q4. This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
#     The first 5 numbers of the sequence, or dots, are:
#     1, 3, 6, 10, 15
#     This means that the first triangle has just one dot, the second one has three dots, the third one
#     has 6 dots and so on.
#     Write a function that gives the number of dots with its corresponding triangle number of the
#     sequence.

def triangle(dot):
    return dot*(dot+1)//2

tr = int(input("How many triangles? -> "))
print(triangle(tr))


# Q5. Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
#     returns the missing number.

def missing_num(l):
    return (i for i in range(1,11) if i not in l)

lst = [1,2,4,5,6,7,8,9,10]
print(next(missing_num(lst)))
