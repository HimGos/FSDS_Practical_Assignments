# Q1. Write a Python Program to find sum of array?

def arrsum(ar):
    return sum(ar)

arr = [2,3,4,5,6]
find_sum = arrsum(arr)
print(find_sum)


# Q2. Write a Python Program to find largest element in an array?

def lar(ar1):
    return max(ar1)

arr1 = [23,12,54,34,21,5,60,59]
find_max = lar(arr1)
print("\nLargest Element in array: ",find_max)


# Q3. Write a Python Program for array rotation?

def rot(ar2,tim):
    i = 1
    while i <= tim :
        ar2.append(ar2[0])
        ar2.pop(0)
        i +=1
    return ar2

arr2 = [1,2,3,4,5,6]
rot_time = int(input("\nHow many times you want to rotate the array? : "))
rotation = rot(arr2,rot_time)
print(rotation)


# Q4. Write a Python Program to Split the array and add the first part to the end?

def spl(ar3,pos):
    temp_arr = []
    split_till = ar3[0:pos]
    for i in split_till:
        temp_arr.append(i)
    for i in range(pos):
        ar3.pop(0)
    ar3 += temp_arr
    return ar3

arr3 = [1,2,3,4,5,6,7,8]
print(f"\nOriginal String: {arr3}")
cut_till = int(input("Specify the position upto which you wanna split the list from: "))
spliting = spl(arr3,cut_till)
print(f"New String after moving split part to end: {spliting}")


# Q5. Write a Python Program to check if given array is Monotonic?

def mon(ar4):
    if ar4 == sorted(ar4) or ar4 == sorted(ar4,reverse=True):
        return "\nMonotonic"
    else:
        return "\nNot Monotonic"

arr4 = [66,55,44,44,43,22,2]
mono_check = mon(arr4)
print(mono_check)