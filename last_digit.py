# "Write a program to take a positive number from the user and then display the last digit of that number.
        
# Test Case1:
# Input:
# 843
# Output:
# 3

# Test Case2:
# Input:
# 321
# Output:
# 1
# "





num=int(input("Enter the number.:- "))
last_digit=num%10
print(last_digit)