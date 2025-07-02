# "Write a program to take two inputs from the user and swap them without using a temporary or third variable.

# Test Case1:
# Input:
# 2
# 3
# Output:
# 3
# 2
# "



num1=int(input("Enter the value of num1. :- "))
num2=int(input("Enter the value of num2 :- "))
num1=num1+num2
print(num1)
num2=num1-num2
print(num2)
num1=num1-num2
print(num1)
print("First value is",num1,"second value is",num2)