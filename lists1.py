# Practicing List

# List of names

# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# print("List of names:", names)

# Append a new name to the list
# There are two ways to append a new name to the list. 
# The first way is to use the append() method, which adds the new name to the end of the list. 
# The second way is to use the insert() method, which allows you to specify the 
# index at which you want to insert the new name.

# names.append("Frank")
# print("After appending a new name:", names)

# names.append("Grace")
# print("After appending another new name:", names)

# # Now we will add new name with insert method

# names.insert(2, "Hannah")
# print("After inserting a new name at index 2:", names)

# names.insert(5, "Ivy")
# print("After inserting another new name at index 5:", names)

# ---------------------------------------------------------------------------------------------

# Copy a list
# There are two ways to copy a list
# First is copy by value
# Second is copy by reference
# First we will copy by value

# num_list = [1, 2, 3, 4, 5]
# print("Original list:", num_list)

# Copying by value

# num_list_copy = num_list.copy()
# print("Copied list (by value):", num_list_copy)

# Copy by reference
# num_list_ref = num_list
# print("Reference list (by reference):", num_list_ref)

# Lets add a new element to the original list and see how it affects the copied lists

# num_list.append(6)
# print("After appending a new element to the original list:", num_list)
# print("Copied list (by value):", num_list_copy)
# print("Reference list (by reference):", num_list_ref)

# ---------------------------------------------------------------------------------------------------

# Counting elements of list

# num_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print("Original list:", num_list)

# Counting the number of occurrences of a specific element in the list
# count = num_list.count(2)
# print("Number of occurrences of 2:", count)

# count1 = num_list.count(4)
# print("Numer of occurrences of 4:", count1)

# ----------------------------------------------------------------------------------------------------

# Reversing a list
# num = [1, 2, 3, 4, 5]
# print("Original list:", num)

# num.reverse()
# print("Reversed list:", num)

# ----------------------------------------------------------------------------------------------------

# Removing elements from a list

# num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list:", num1)

# Removing an element by value
# num1.remove(5)
# print("After removing 5 from the list:", num1)

# num1.remove(8)
# print("After removing 8 from the list:", num1)

# ----------------------------------------------------------------------------------------------

# Sorting a list

# num2 = [5, 2, 9, 1, 5, 6]
# print("Original list:", num2)

# Sorting the list in ascending order
# By default, the sort() method sorts the list in ascending order.
# num2.sort()
# print("Sorted list in ascending order:", num2)

# Lets sort the list in descending order

# num2.sort(reverse = True)
# print("Sorted list in descending order:", num2)

# ----------------------------------------------------------------------------------------------

# Popping elements from a list

# num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list:", num3)

# Popping an element from the end of the list
# By default, the pop() method removes and returns the last element of the list.

# popped_element = num3.pop()
# print("Popped element from the end of the list:", popped_element)

# Lets pop an element from a specific index
# popped_element_index = num3.pop(3)
# print("Popped element from index 3:", popped_element_index)

# popped_element_index1 = num3.pop(5)
# print("Popped element from index 5:", popped_element_index1)

# ----------------------------------------------------------------------------------------------

# Extending a list
# Extending a list means adding elements from another list to the end of the original list.

# num4 = [1, 2, 3, 4, 5]
# print("Original list:", num4)

# num5 = [6, 7, 8, 9, 10]
# print("List to be added:", num5)

# num4.extend(num5)
# print("After extending the original list with the new list:", num4)

# ----------------------------------------------------------------------------------------------

# Clearing a list
# Clearing a list means removing all elements from the list.

# num6 = [1, 2, 3, 4, 5]
# print("Original list:", num6)

# num7 = [6, 7, 8, 9, 10]

# num6.extend(num7)
# print("After extending the original list with the new list:", num6)

# num6.clear()
# print("After clearing the list:", num6)

# ----------------------------------------------------------------------------------------------

# Slicing a list
# Slicing a list means extracting a portion of the list based on specified indices.

# students_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy"]
# print("Original list of student names:", students_names)

# Slicing the list to get the first three names
# If you want to slice a list to get the first three names, you can use the slicing syntax: list[start:end].

# first_three_names = students_names[0:3]
# print("First three names:", first_three_names)

# If you want to get the exact index then add +1 to the end index.

# first_four_names = students_names[0:5]
# print("First four names:", first_four_names)

# List of 20 numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Original list of numbers:", numbers)

# Stepping through the list.

num = numbers[0:5:2]  # This will give us the first five numbers with a step of 2.
print(num)
