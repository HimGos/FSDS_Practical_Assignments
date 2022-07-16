# Q1. Write a function that takes a list and a number as arguments. Add the number to the end of the list,
#     then remove the first element of the list. The function should then return the updated list.

def next_in_line(lst,num):
    if len(lst) == 0 :
        return "No list has been selected"
    else :
        lst.pop(0)
        lst.append(num)
        return lst

res1 = next_in_line([5,6,7,8,9], 1)
print(res1)


# Q2. Create the function that takes a list of dictionaries and returns the sum of people's budgets.

def get_budgets(dict_list):

    return sum([dic['budget'] for dic in dict_list if 'budget' in dic])


d = [ {'name': "john", "age":21, "budget":23000}, {'name': "Steve", "age":32, "budget":40000}
      , {'name': "Martin", "age":16, "budget":2700}]

res2 = get_budgets(d)
print(res2)


# Q3. Create a function that takes a string and returns a string with its letters in alphabetical order.

def alphabet_soup(st):
    return "".join(sorted(st))

res3 = alphabet_soup('hello')
print(res3)


# Q4. Create a function that accepts the principal p, the term in years t, the interest rate r, and the
#     number of compounding periods per year n. The function returns the value at the end of term
#     rounded to the nearest cent.

def compound_interest(p,t,r,n):
    formula = p*((1+(r/n))**(n*t))
    return round(formula, 2)

res4 = compound_interest(10000, 10, 0.06, 12)
print(res4)


# Q5. Write a function that takes a list of elements and returns only the integers.

def return_only_integer(l):
    return [i for i in l if type(i)==int]

res5 = return_only_integer(['lion', 'giraffe', 4, 3.5,'merc', 5])
print(res5)