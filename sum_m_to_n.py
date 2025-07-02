# Write a program to take two integers M, and N and print the sum of numbers in the range M to N.

# Test Case1:
# Input:
# 2
# 7
# Output:
# 27
# Explanation:
# Output should be 27 as the sum of numbers (2+3+4+5+6+7=27)



m=int(input("Enter the value of M. :- "))
n=int(input("Enter the value of N. :- "))
if m>n:
    max=m
    min=n
else:
    max=n
    min=m
sum=0
while min<=max:
    sum=sum+min
    min=min+1
print(sum)