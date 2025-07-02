# "Write a program to take two numbers from the user and perform Six basic operations (addition, subtraction, multiplication, division, integer division and modulus) on those two numbers.
        
# Note: Print the output in the order as mentioned in the question.

# Test Case1:
# Input: 
# 12 
# 5
# Output: 
# 17
# 7
# 60
# 2.4
# 2
# 2
# "

num1=int(input("Enter the num1. :- "))
num2=int(input("Enter the num2. :- "))
addition=num1+num2
multiplication=num1*num2
division=num1/num2
integer_division=num1//num2
reminder=num1%num2
print("addition is",addition,"multiplication",multiplication,"division",division,"integer division",integer_division,"reminder",reminder)