 
 	
# Write a program to take an integer as input and print the smallest positive integer that is a multiple of both 2 and n.

# Test Case:
# Input:
# 5
# Output:
# 10

# Test Case:
# Input:
# 6
# Output:
# 6






num=int(input("Enter the value. :- "))
if num%2==0:
    print(num)
elif num%2!=0:
    print(num*2)
else:
    print("Error")