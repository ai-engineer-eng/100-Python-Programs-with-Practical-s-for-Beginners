# #Solution 01 - (using exponentiation)

# num = int(input("Enter your number: "))         #taking number from user

# sr = num**(1/2)                                 #initialized a sr variable and using exponentiation method to find square root of user numberand storing to variable

# print("Square root of given number is: ", sr)   #print square root of number with message.



# #Solution 02 - (using math module)

import math

num = int(input("Enter your number: "))

sr = math.sqrt(num)

print("Square root of the given number is: ", sr)