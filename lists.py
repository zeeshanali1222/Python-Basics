# Practice Lists in Python

names = ["Ali", "Ahmed", "Hassan", "Hussain"]
print(names)

fruits = []
print(fruits)

# Adding elements to the list
# First method to add elements to the list is using append() method
# Append method adds the element at the end of the list
# We can only add one value in append function

fruits.append("Apple")
print(fruits)

fruits.append("Banana")
print(fruits)

# Second method to add elements to the list is using insert() method
# Insert method adds the element at the specified index
# We can only add one value in insert function

fruits.insert(1, "Mango")
print(fruits)

fruits.insert(2, "Guava")
print(fruits)

# How can we add multiple values to the list at once?
# We can use extend() method to add multiple values to the list at once

fruits.extend(["Orange", "Pineapple", "Grapes"])
print(fruits)

# How can we count the specific element in the list?
# We can use count() method to count the specific element in the list

fruit_count = fruits.count("Apple")
print(fruit_count)

fruit_count1 = fruits.count("Banana")
print(fruit_count1)

# Methods to copy the list
# First method to copy the list is using copy() method
# Copy method creates a shallow copy of the list
# Its called Copy by Value. That means if we change the value of the copied list, 
# it will not affect the original list

fruits_copy = fruits.copy()
print(fruits_copy)

# Second method to copy the list is simply assigning the list to a new variable
# This method creates a reference to the original list
# Its called Copy by Reference. That means if we change the value of the copied list,

fruits_copy1 = fruits
print(fruits_copy1)

# For example, if we change the value of the copied list, it will affect the original list

fruits.append("Strawberry")
print(fruits)

# Lets see if our copied list is affected or not

print(f"Our Original List: {fruits_copy}")
print(f"Reference List: {fruits_copy1}")