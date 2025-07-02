# Write a program to take a number from the user and print the sum of the digits of the given number.

# Test Case1:
# Input:
# 456
# Output:
# 15
# Explanation:
# 4+5+6 = 15



num=int(input("ENter the Number. :- "))
sum=0
while num!=0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)