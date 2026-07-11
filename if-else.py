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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# print(1>3)

# a = 10
# b = 20

# if a > b:
#     print(f"{a} is greater than {b}.")
# else:
#     print(f"{b} is greater than {a}.")

# -----------------------------------------------------------------------

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------


class Mohsin():
    def __init__(self , name , age , gender , history ):
        self.name     = name
        self.age      = age
        self.gender   = gender
        self.history  = history
myclass = Mohsin( name = 'mOHSIN' , age = 21 , gender = 'Male' , history = 'Okara' )
print( myclass.name )
print( myclass.age )
print( myclass.gender )


# Classs Attributes and Methods(A function defined inside any class)
# What is difference between function and Method.

class Dog():
    alpha = 'Bravo'
    def __init__(self , name , age ):
        self.name = name
        self.age  = age
    def bark( self , number ):
        print('The quick brown fox jumps over a lazy dog.!')
        print('my name is {} and number is {}'.format( self.name , number))
        
mydog = Dog( 'Mohsin' , 21 )

print( mydog.name )
print( mydog.age )
# Attribute calling when we put  "mydog.bark" without "()" It means we are calling an attribute.
print( mydog.bark )
# Method   calling ( Whenever we call method we need to put " mydog.bark() " )
print( mydog.bark(12) )


# Write a class too calculate area of circle.

class Circle():
    pi = 3.14
    # Function for class object Attribute
    def __init__(self , radius = 1 ):
        self.radius = radius
    # Function for Methods
    def get_circumference(self):
        return self.pi * self.radius ** 2
area = Circle()
print(area.pi)
print(area.radius)
area = Circle(23)
print(area.radius)

print(area.get_circumference)

print( area.get_circumference() )
print( f' The area is {area.get_circumference()} sqare units' )

# Anotyher Approach for same
class Circle():
    pi = 3.14
    # Function for class object Attribute
    def __init__(self , radius  ):
        self.radius = radius
        self.area = self.radius ** 2 * Circle.pi
    # Function for Methods
    def get_circumference(self):
        return self.pi * self.radius ** 2
circle_area = Circle(20)
area = Circle(20)
print( area.pi )
print( area.radius )
print( area.area )

# Inheritance Examples(Way to form new classes using classes  already  been  defined)
# Reuse code and reduce complexity of code
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print('I am an animal.')
    def eat(self):
        print(" Animal eating.")
main_class = Animal()
print(main_class)

# Child Class

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created.')
    # Redefining
    def who_am_i(self):
        print('I am a dog. ')
    def eat(self):
        print('Dog is eating.')
    # a new method
    def bark(self):
        print(' Dog is barking!  ') 
        

mydog = Dog()
print(mydog)
print(mydog.bark())
print(mydog.who_am_i())
print(mydog.eat())

# Ploymorphism

class Cat():
    def __init__(self , name ):
        self.name = name
    def speak(self):
        return self.name + " speaks Meaaoo'n   "

class Dog():
  
    def __init__(self, name ):
        self.name = name
    def speak(self):
        return self.name + "  speaks Vaao00'f   "

poly = Cat('Billi')
print(poly.speak())
morphism = Dog('Kutta')
print(morphism.speak())

# Implementing Poymorphism using for loop
for i in [ poly , morphism ]:
    print(type(i))
    print(type(i.speak()))
    
# Implementing Poymorphism using for Functions.
def pet_speak( i ):
    print(i.speak())
a = pet_speak( poly ) 
b = pet_speak( morphism )
print( a , b )

# Another Polymorphism Approach
class Animal():
    def  __init__( self , name ):
        self.name  = name
    def speak():
        raise NotImplementedError("Subclass must implement this abstract method.")
    
class Dog(Animal):
    def speak(self,name):
        return self.name + " says Wooo'f "
    
class Cat(Animal):
    def speak(self,name):
        return self.name + " says Meaaooo'n "
    
mycat = Cat('  Billy:  ')
mydog = Dog('  Kutta:  ')

        
print(mycat.speak('Waao'))

print(mydog.speak('Meao'))

# Special Magic Dunder Methods

class Book():
    def __init__( self , name , author , pages ):
        self.name = name 
        self.author = author
        self.pages = pages
    def __str__(self):
        return f' The book {self.name} by author {self.author} has {self.pages} pages. '
    def __del__(self):
        print('Book has been Deleted')
        
    
    
mybook = Book('AI Superpwers' , 'Kai-Fu-Lee' , 300 )
print(mybook)

# del mybook
# print(mybook)

    