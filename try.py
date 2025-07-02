# # rows=int(input("Enter how many stars you want in last line. :- "))
# # for i in range(rows):
# #     print(" " * (rows*i))
# #     print ( " *" * (i))



















# rang=int(input("Enter the range of numbers :- "))
# array=[]
# for i in range(rang):
#     num=int(input("Enter the value :- "))
#     array.append(num)
# print(array)
# i=0
# j=1
# count=1
# v=0
# while 1<rang:
#     while j<rang:
#         if array[i]==array[j]:
#             v+=1
#         j+=1
#     i+=1
#     j=count
#     count+=1
#     v=0
#     print(array[i],v)














# sum=0
# for i in range(50):
#     if i%2==0:
#         sum=sum+i
# print(sum)













# num=34
# while num!=1:
#     num=num//2
#     print(2)









# # Step 1: दो अव्यवस्थित (unsorted) सूचियाँ बनाई गई हैं
# arr1 = [13, 23, 325, 723]
# arr2 = [232, 4, 43, 8, 10]

# # Step 2: दोनों सूचियों को जोड़कर (merge करके) एक नई सूची बनाई
# merged = arr1 + arr2  # arr1 और arr2 को जोड़कर merged नाम की नई list बनाई गई

# # Step 3: मर्ज की गई सूची को manually sort करेंगे (bubble sort का उपयोग करके)
# n = len(merged)  # merged सूची की कुल लंबाई (total elements) n में रखी गई

# # Outer loop: पूरी सूची को n बार चेक करेगा
# for i in range(n):
    
#     # Inner loop: हर बार दो दो संख्याओं की तुलना करेगा और बड़ी संख्या को आगे भेजेगा
#     for j in range(0, n - i - 1):
        
#         # अगर पहले वाली संख्या, अगली संख्या से बड़ी है तो दोनों की जगह बदलो
#         if merged[j] > merged[j + 1]:
#             # Swap: बड़ी संख्या को पीछे भेजना
#             merged[j], merged[j + 1] = merged[j + 1], merged[j]

# # Step 4: अंत में पूरी तरह से क्रमबद्ध (sorted) सूची को प्रिंट किया गया
# print("Sorted Merged Array (without sort()):", merged)  # अंतिम sorted सूची को print किया गया
































# # Step 1: User se arr1 ka input lena
# size1 = int(input("Array 1 ke kitne elements hain? :- "))
# arr1 = []  # arr1 list bana rahe hain
# print("Array 1 ke elements dijiye:")

# for i in range(size1):
#     num = int(input(f"Element {i+1} :- "))
#     arr1.append(num)  # har inputted number ko arr1 mein add kar rahe hain

# # Step 2: User se arr2 ka input lena
# size2 = int(input("Array 2 ke kitne elements hain? :- "))
# arr2 = []  # arr2 list bana rahe hain
# print("Array 2 ke elements dijiye:")

# for i in range(size2):
#     num = int(input(f"Element {i+1} :- "))
#     arr2.append(num)  # har inputted number ko arr2 mein add kar rahe hain

# # Step 3: Merge both arrays
# merged = arr1 + arr2  # dono arrays ko jod diya

# # Step 4: Manually sort karna (Bubble Sort)
# n = len(merged)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if merged[j] > merged[j + 1]:
#             # Swap
#             merged[j], merged[j + 1] = merged[j + 1], merged[j]

# # Step 5: Output
# print("Sorted Merged Array (without sort()):", merged)


















# # Step 1: User se ek number lena
# num = int(input("Enter a number to check if it's prime: "))             
# # Step 2: Prime number check karne ke liye flag variable
# is_prime = True  # Assume the number is prime initially 
# # Step 3: 2 se lekar number ke square root tak check karna
# for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:  # Agar number i se divide hota hai
#         is_prime = False  # Toh number prime nahi hai
#         break  # Loop ko break kar do   
# # Step 4: Result print karna
# if is_prime and num > 1:  # Agar number prime hai aur 1 se bada hai
#     print(f"{num} is a prime number.")
# else:  # Agar number prime nahi hai ya 1 se chhota hai
#     print(f"{num} is not a prime number.")  # Toh number prime nahi hai







# # Program to print a pattern of numbers in a triangle shape
# r = int(input("Enter the range: "))
# r=r+1
# i = 1
# while i <= r:
#     n = 1
#     while n < i:
#         print(n, end='')
#         n += 1
#     print()
#     i += 1












# r = int(input("Enter the range: "))
# r=r+1
# n=1
# i = n+1
# k=i+1
# while i <= r:
#     while n < i:
#         print(n, end='')
#         n += 1
#         k+=1
#     print()
#     i += 2
#     i=k















# #
# r = int(input("Enter the number of rows: "))
# n = 1
# i = 1

# while i <= r:
#     j = 1
#     while j <= i:
#         print(n, end=' ')
#         n += 1
#         j += 1
#     print()
#     i += 1