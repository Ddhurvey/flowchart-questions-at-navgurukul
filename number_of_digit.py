 
 	
# Write a program to take a number from the user and print the number of digits in the given number. 

# Test Case1:
# Input:
# 456
# Output:
# 3


num=int(input("ENter the Number. :- "))
count=0
while num!=0:
    num=num//10
    count+=1
print(count)