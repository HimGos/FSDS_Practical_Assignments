# Q1. Create a function that takes an integer and returns a list from 1 to the given number, where:
#       1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
#       2. If the number cannot be divided evenly by 4, simply return the number.

def amplify(n):
    return [i*10 if i%4==0 else i for i in range(1,n+1)]

print(amplify(25))


# Q2. Create a function that takes a list of numbers and return the number that's unique.

def unique(nl):
    return [i for i in set(nl) if nl.count(i)==1]
    # for i in set(nl):
    #     if nl.count(i) == 1:
    #         return i

print(unique([0,1,1,1,1]))


# Q3. Your task is to create a Circle constructor that creates a circle with a radius provided by an
#     argument. The circles constructed must have two getters getArea() (PIr^2) and
#     getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

class Circle:
    def __init__(self,rad):
        self.rad = rad

    def getArea(self):
        return 3.14159*(self.rad**2)

    def getPerimeter(self):
        return 2*3.1415*self.rad

circ = Circle(11)
print(circ.getArea())

circ2 = Circle(4.44)
print(circ2.getPerimeter())


# Q4. Create a function that takes a list of strings and return a list, sorted from shortest to longest.

def sort_by_length(l):
    return sorted(l,key=len)

res = sort_by_length(["Turing","Einstein","Jung","Apple"])
print(res)


# Q5. Create a function that validates whether three given integers form a Pythagorean triplet. The
#       sum of the squares of the two smallest integers must equal the square of the largest number to
#       be validated.

def is_triplet(a,b,c):
    l = [a,b,c]
    greatest = max(l)**2
    l.remove(max(l))
    if greatest == l[0]**2 + l[1]**2:
        return True
    else:
        return False

res2 = is_triplet(13,5,12)
print(res2)