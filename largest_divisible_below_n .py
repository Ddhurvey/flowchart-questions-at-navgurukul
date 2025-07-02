# Write a program to take two numbers, A and B from the user. Your task is to find the largest number that is less than A and can be divided evenly by B. Can you figure out that number?

# Test Case1:
# Input:
# 15
# 4
# Output:
# 12

# Test Case2:
# Input:
# 27
# 5
# Output:
# 25



a=int(input("Enter the value of A. :- "))
b=int(input("Enter the value of B where B is less than A. :- "))
sum=(a-1)//b
sum2=sum*b
print("Largest divisble number below N is",sum2)