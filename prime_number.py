# Write a program to check if a number is a special type of number called a 'prime number'. A prime number is a number that is only divisible by 1 and itself, and it doesn't have any other factors. 
# For example, the number 7 is a prime number because it can only be divided by 1 and 7 without leaving a remainder. However, the number 12 is not a prime number because it has other factors, such as 2, 3, 4, and 6, in addition to 1 and 12. (Take the number from the user)? Learn sieve algorithm

# Test Case1:
# Input:
# 97
# Output:
# Yes 

# Test Case2:
# Input:
# 49
# Output:
# No







num=int(input("Please Enter the Number.:- "))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(num,"is prime number.")
else:
    print(num,"is not a prime number.")
    