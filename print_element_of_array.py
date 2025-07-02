# Write a program to print all the numbers from the given array using a loop. 
# L = {23, 45, 32, 25, 46,33, 71, 90}

# Output:
# 23
# 45
# 32
# 25
# 46
# 33
# 71
# 90



rang=int(input("Enter the range of number. :- "))
a=[]
for i in range(rang):
    value=int(input("enter the value:- "))
    a.append(value)
for i in range(rang):
    print(a[i])