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