# Input dimensions and the condition value n
x = 1

y = 2

z = 3

n = 4

# Initialize an empty list to store the coordinates
# coordinates = []

# # Use nested loops to generate all possible coordinates
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):

#             # Check if the sum of i, j, and k is not equal to n
#             if (i + j + k != n):

#                 # If valid, add the coordinate to the list
#                 coordinates.append((i, j, k))

# Print the resulting list of coordinates
# print(coordinates)


#with list comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())   
    
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if x + y + z != n]
    
    print(coordinates)