# Code to check eligibility for voting based on age

# voter_age = int(input("Enter your age: "))

# if voter_age >= 18:
#     print("You are eligible to vote. ")
# else:
#     print("You are not eligible to vote. ")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Code to check if number is divisible by 7

# number = int(input("Enter a number: "))

# if number % 7 == 0:
#     print(f"{number} is divisible by 7." )
# else:
#     print(f"{number} is not divisible by 7." )

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to display "Hello" if number is divisible by 5, otherwise print "Bye".

# number = int(input("Enter a number: "))

# if number % 5 == 0:
#     print("Hello")
# else:
#     print("Bye")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to calculate the electricity bill (accept number of units from user) according to the following criteria:
# First 100 units: no charge
# Next 100 units: Rs 5 per unit
# After 200 units: Rs 10 per unit
# For example if input unit is 350 than total bill amount is Rs. 1500.

# a = 0
# number_of_units = int(input("Enter number of units: "))

# if number_of_units <= 100:
#     a = 0
# elif number_of_units <= 200:
#     a = (number_of_units - 100) * 5
# else:
#     a = (100 * 5) + (number_of_units - 200) * 10
# print(f"Your Total bill is: $ {a}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to display the last digit of a number.
# For example any number % 10 will return the last digit of that number.

# a = int(input("Enter a number: "))
# print(f"The last digit of {a} is: {a % 10}" )

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday etc.

# day_number = int(input("Enter a number from 1 to 7: "))
# if day_number == 1:
#     print("Sunday")
# elif day_number == 2:
#     print("Monday")
# elif day_number == 3:
#     print("Tuesday")
# elif day_number == 4:
#     print("Wednesday")
# elif day_number == 5:
#     print("Thursday")
# elif day_number == 6:
#     print("Friday")
# elif day_number == 7:
#     print("Saturday")
# else:
#     print("Invalid input. Please enter a number from 1 to 7.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to check whether a number is positive, negative or zero.

# a = int(input("Enter a number: "))

# if a > 0:
#     print(f"{a} is a positive number. ")
# else:
#     print(f"{a} is a negative number. ")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program to check a character is vowel or consonant.

# char = input("Enter a character: ")
# vowels = "aeiouAEIOU"

# if char in vowels:
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is a consonant.")

# --
# -----------------------------------------------------------------------------------------------------------------------------------------------------------