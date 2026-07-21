# Practicing For Loop in Python

# for a in range(10): # By default it will the start the value from 0
#     print(a)

# for b in range(1, 10): # It will start the number from 1
#     print(b)

# cities = ["FSD", "LHR", "KHI", "MLT", "HYD", "BHL"]

# for city in cities:
#     print(city)

# If we give only one string value to a variable the it print the characters of that value

# a = "Pakistan"

# for char in a:
#     print(char)

# As soon as we give more than one string value then it take as tuple

# a = "Pakistan", "Lebanon", "Syria"
# print(a)

# for d in a:
#     print(d)

# Break and Continue functions in For Loop

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(num)

# for a in num:
#     if a % 2 == 0:
#         print("It is an even number: ", a)
#     else:
#         print("It is an Odd number: ", a)

# Wrong code below

# num = input("Enter any number: ")
# print(num)

# for a in num:
#     if a % 2 == 0:
#         print("It is an even number: ", a)
#     else:
#         print("It is an Odd number: ", a)

# Dislaying descending numbers

# num = list(range(1, 11))
# print("Original List ", num)

# print("\nReversed List \n")

# for a in reversed(num):
#     print(a)

# Taking a number from user and adding 1 in it

# num = int(input("Enter any Numner: "))

# for i in range(1, num + 1):
#     result = i + 1
# print(f"Orginal Number: {i} --> After adding 1: {result}")

# Taking a number from user and then making a table of that number

# num = int(input("Enter any number: "))

# for i in range(1, 11):
#     result = num * i
#     print(f"{num} x {i} = {result}")

# Take a number from user and make a cube of it

# num = int(input("Enter any number: "))

# for i in range(1, num + 1):
#     print(f"Current Number is {i} and Cube is {i ** 3}")

# for i in range(1, 10):
#     print(i)

# for i in range(4):
#     x = int(input("Enter a number between 1 and 100: "))
#     if i <= x <= 100:
#         print("Valid Nnumber: ", x)
#         break
#     else:
#         print("Invalid Number: ", x)