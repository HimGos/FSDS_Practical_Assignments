# Q1. Create a function that takes a string and returns a string in which each character is repeated once.

def rep(s):
    final_string = ""
    for i in range(len(s)):
        final_string += s[i]*2
    return final_string

st_inp = input("Enter a string to double it's characters: ")
print(rep(st_inp))


# Q2. Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
#     if another variable type is given.

def bol(var):
    if type(var)==bool:
        return not var
    else :
        return "boolean expected"

res = bol(0)
print(res)



# Q3. Create a function that returns the thickness (in meters) of a piece of paper after folding it n
#     number of times. The paper starts off with a thickness of 0.5mm.

def num_layers(fold):
    return (2**fold)/2000

paper_fold = int(input("How many times you folded the paper? ->  "))
print(f"Thickness after {paper_fold} folds", num_layers(paper_fold),'m')



# Q4. Create a function that takes a single string as argument and returns an ordered list containing
#     the indices of all capital letters in the string.

def index_of_caps(s1):
    return [i for i in range(len(s1)) if s1[i].isupper()]

s1 = input("Enter your string to find indices of all capital leters: ")
print(index_of_caps(s1))



# Q5. Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

def find_even_nums(n):
    return [i for i in range(2,n+1,2)]

eves = int(input("Till where you want even numbers list: "))
print(find_even_nums(eves))