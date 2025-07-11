# Imagine you're responsible for calculating electricity bills for households. Each household consumes electricity, and the bill varies based on the number of units consumed. The bill calculation involves different rates for different ranges of units consumed, along with an additional surcharge.

# Write a program  to input electricity unit charges and calculate the total electricity bill according to the given condition:
# For the first 50 units Rs. 0.50/unit
# For the next 100 units Rs. 0.75/unit
# For the next 100 units Rs. 1.20/unit
# For units above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

# Tips:

# 1. Understand how the bill amount varies for different ranges of units consumed.
# 2. Pay attention to adding the surcharge correctly to the total bill amount.
# 3. Ensure accuracy in calculations and handle different scenarios effectively.

# Test Case1:
# Input:
# 200
# Output:
# 192

# Imagine you're responsible for calculating electricity bills for households. Each household consumes electricity, and the bill varies based on the number of units consumed. The bill calculation involves different rates for different ranges of units consumed, along with an additional surcharge.

# Write a program  to input electricity unit charges and calculate the total electricity bill according to the given condition:
# For the first 50 units Rs. 0.50/unit
# For the next 100 units Rs. 0.75/unit
# For the next 100 units Rs. 1.20/unit
# For units above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

# Tips:

# 1. Understand how the bill amount varies for different ranges of units consumed.
# 2. Pay attention to adding the surcharge correctly to the total bill amount.
# 3. Ensure accuracy in calculations and handle different scenarios effectively.

# Test Case1:
# Input:
# 200
# Output:
# 192



units=int(input("Enter the value in Units. :- "))  # User ne 200 unit electricity use kiya

# Step 1: Pehle check karte hain total units kis slab mein aate hain
if units <= 50:
    bill = units * 0.50  # Agar 50 ya usse kam units hain
elif units <= 150:
    bill = (50 * 0.50) + (units - 50) * 0.75
    # Pehle 50 units * 0.50 = 25
    # Baaki (200 - 50 = 150) * 0.75 = 150 * 0.75 = ₹112.5 (BUT yeh case apply nahi hoga kyunki 200 > 150)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
    # 50 * 0.50 = ₹25
    # 100 * 0.75 = ₹75
    # 200 - 150 = 50 units * 1.20 = ₹60
    # bill = 25 + 75 + 60 = ₹160
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50
    # Yeh case tab hota jab units > 250 hote. 200 ke liye yeh nahi chalega.

# Step 2: Surcharge calculate karna (20% of bill)
surcharge = bill * 0.20
# surcharge = 160 * 0.20 = ₹32

# Step 3: Final total
total = bill + surcharge
# total = 160 + 32 = ₹192

# Step 4: Output
print("Your electricity bill is: ₹", round(total, 2))
