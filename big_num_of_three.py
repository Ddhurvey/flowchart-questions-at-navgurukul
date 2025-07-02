 
 	
# Write a program to take three numbers from the user and print the greater number of the three numbers. (Assume all three numbers are distinct)

# Test Case1:
# Input:
# 20
# 3
# 43
# Output:
# 43



num1=int(input("Enter the Value of Num1. :- "))
num2=int(input("Enter the Value of Num2. :- "))
num3=int(input("Enter the Value of Num3. :- "))
if num1>num2:
    max=num1
    smax=num2
else:
    max=num2
    smax=num1
if max>num3:
    if smax>num3:
        tmax=num3
    else:
        tmax=smax
        smax=num3
else:
    tmax=smax
    smax=max
    max=num3
print("max is ",max," second max is ",smax," and third max is ",tmax)