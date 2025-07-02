# Write a program to take size of array, array and target as input from the user and check whether the target exists in this array or not.

# Test Case1:
# Input:
# 7
# 1 2 3 4 5 6 7
# 3
# Output:
# Yes

# Test Case2:
# Input:
# 8
# Output:
# No







size = int(input("Enter the size of the array: "))
arra = []

# Taking array input
i = 1
while i <= size:
    arra.append(i)
    i += 1

# Taking target input
target = int(input("Enter the target number: "))

# Checking if target exists in array
if target in arra:
    print("Yes")
else:
    print("No")
