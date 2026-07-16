# Learning Tuples in Python
# Tuples are immutable. Means a tuple cannot be changed
# We cannot add or remove a value in a tuple
# We can only perform Count and Index functions in tuples

atuple = ("Ali", 100, "Ali", 200, "Hamdan", "Armish", "Hamdan")
print(atuple)

a = atuple.count("Hamdan")
print("Count the occurence of name Hamdan: ", a)

b = atuple.index("Hamdan")
print("Index of name Hamdan is: ", b)