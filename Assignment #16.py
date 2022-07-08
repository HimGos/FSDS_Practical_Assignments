# Q1. Write a function that stutters a word as if someone is struggling to read it. The
#     first two letters are repeated twice with an ellipsis ... and space after each, and then the
#     word is pronounced with a question mark ?.

def stut(word):
    st_word = word[:2]
    return (st_word + '...')*2 + word + '?'

result = stut('incredible')
print(result)


# Q2. Create a function that takes an angle in radians and returns the corresponding
#     angle in degrees rounded to one decimal place.

def rad2deg(rad):
    return rad * (180/3.14)

res = rad2deg(1)
print(f"Radian to degree -> {res}")


# Q3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus
# 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
# number.

# Given a non-negative integer num, implement a function that returns True if num is a Curzon
# number, or False otherwise.

def curz(num):
    if (2**num+1) % (2*num+1) == 0:
        return True
    else :
        return False

curzcheck = curz(14)
print(curzcheck)



# Q4. Given the side length x find the area of a hexagon.

def hex(side):
    return (3*(3**0.5)*(side*side))/2

hexcheck = hex(2)
print(hexcheck)



# Q5. Create a function that returns a base-2 (binary) representation of a base-10
# (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
# 010101001(2) = 1 + 8 + 32 + 128.

# Going from right to left, the value of the most right bit is 1, now from that every bit to the left
# will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

def bin2dec(n):
    return bin(n).replace('0b',"")

bincheck = bin2dec(5)
print(bincheck)