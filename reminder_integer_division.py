# "Write a program to take two numbers A and B from the user and calculate the quotient and remainder when number A is divided by number B.

# Note: Print the output in the order as mentioned in the question.

# Test Case1:
# Input:
# 12
# 5
# Output:
# 2
# 2

# Test Case2:
# Input: 
# 15
# 6
# Output:
# 2
# 3
# "



num1=int(input("Enter the value of num1.:- "))
num2=int(input("Enter the value of num2.:- "))
reminder=num1%num2
integer_division=num1//num2
print("reminder is",reminder,"integer division is",integer_division)