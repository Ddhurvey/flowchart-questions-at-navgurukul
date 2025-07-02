 
 	
# Write a program to take N numbers from a user as input and then print the duplicates in those N numbers. Also, take N as an input from the user.

# Test Case 1:
# Input:
# 5
# 2 4 2 6 3
# Output:
# 2

# Test Case 2:
# Input:
# 6
# 2 4 6 3 3 2
# Output:
# 3 2







array = [2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,8,4,5,8,9,10,11,12,13,4,11]
i = 0
d = []

while i < len(array):
    j = i + 1
    while j < len(array):
        if array[i] == array[j] and array[i] not in d:
            d.append(array[i])
        j += 1
    i += 1

print(d)
