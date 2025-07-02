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



unit=int(input("Enter the unit of Electricity.:- "))
if unit<=50:
    rupees=unit*0.50
elif unit<=100:
    rupees=unit*0.75
elif unit<=250:
    rupees=unit*1.20
elif unit>250:
    rupees=unit*1.50
else:
    print("Entered value is not valid.")
additional_charge=(20/100)*100
total=additional_charge+rupees
print(total,"Is your electricity charge.")