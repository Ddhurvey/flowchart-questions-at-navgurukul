## Number frequecy counter.py

# Step 1: Kitne numbers chahiye, user se poochho
n = int(input("Kitne numbers chahiye? : "))

# Step 2: Numbers ko ek list me store karo
array = []
for i in range(n):
    # Yahan i+1 ka matlab number ka order hai (1, 2, 3 ...)
    print("Number", i+1, "dijiye: ")
    num = int(input())  # Seedha input le rahe hain bina f-string ke
    array.append(num)

# Step 3: Frequency count karna
checked = []  # Jinki counting ho chuki hai

for i in range(n):
    if array[i] not in checked:
        count = 0
        for j in range(n):
            if array[i] == array[j]:
                count += 1
        print(array[i], "-", count)  # Simple print statement bina f-string ke
        checked.append(array[i])
