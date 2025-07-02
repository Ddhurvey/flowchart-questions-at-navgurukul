# Write a program to calculate the sum of the following series where N is input from the user. 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/N

# Test Case1:
# Input:
# 4
# Output:
# 2.08

n=int(input("Enter the value. :- "))
sum=0
i=1
while i<=n:
    sum=sum+(1/i)
    i+=1
print(sum)