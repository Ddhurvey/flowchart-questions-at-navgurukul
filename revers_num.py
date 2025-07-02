 
 	
# Write a program that takes a number from the user and prints the number that is formed by reversing the digits of the number.

# Test Case1:
# Input:
# 123
# Output:
# 321


num=int(input("Enter the Number. :- "))
reverse=0
reminder=0
while num!=0:
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
print(reverse)
