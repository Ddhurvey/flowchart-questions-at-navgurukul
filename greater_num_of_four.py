# Write a program to take four numbers from the user and print the greater number of the four numbers. (assume all the numbers are distinct).

# Test Case1:
# Input:
# 98
# 13
# 29
# 58
# Output:
# 98

num1=int(input("Enter the num1:- "))
num2=int(input("Enter the num2:- "))
num3=int(input("Enter the num3:- "))
num4=int(input("Enter the num4:- "))
# compare num1 & num2
if num1>num2:
    max=num1
    smax=num2
else:
    max=num2
    smax=num1
# compare Num1,Num2 & Num3
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
# Compare Num1,Num2,Num3 & Num4
if max>num4:
    if smax>num4:
        if tmax>num4:
            fomax=num4
        else:
            fomax=tmax
            tmax=num4
    else:
        fomax=tmax
        tmax=smax
        smax=num4
else:
    fomax=tmax
    tmax=smax
    smax=max
    max=num4
print("max num is ",max," second max is ",smax," third max is ",tmax," & fourth max is ",fomax)
