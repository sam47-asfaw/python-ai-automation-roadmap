'''Python Basics:'''

# Python Data Types

# Integer -> are whole numbers
print("Integer: ", 10) # output: 10

# Float -> are decimal numbers
print("Float: ", 10.5) # output: 10.5

# String -> are sequences of characters
print("String: ", "Hello, World!") # output: Hello, World!

# Boolean -> are True or False values
print("Boolean: ", True) # output: True

# Python Variables

# Variables are used to store data in Python. They can be of different data types.
x = 10
y = 10.5
name = "John"
is_active = True

print("Variable: ", x ) # output: 10
print("Variable: ", y) # output: 10.5
print("Variable: ", name) # output: John
print("Variable: ", is_active) # output: True

# Math Operations in Python

print("Addition: ", 10 + 10) # output: 20
print("Subtraction: ", 10 -5) # output: 5
print( "Multiplication: ", 10 *5) # output: 50
print ("Division: ", 10 / 5) # output: 2
print ("Floor Division: ", 10 // 3) # output: 3
print ("Modulus: ", 10 % 3) # output: 1
print ("Exponentiation: ", 10 ** 3) # output: 1000
print ("Order of Operations: ", 10 + 10 * 10) # output: 110
print ("Order of Operations with Parentheses / BODMAS: ", (10 + 10) * 10) # output: 200



# Python Operations with different data types

print("Integer + Float: ", 10 + 10.5) # output: 20.5
print("String + String: ", "Hello, " + "World!") # output: Hello, World!
print("Boolean: ", (x + y)==22.5) #output: False
#print("String + Integer: ", "Hello, " + 10) # output: TypeError: can only concatenate string with string types
 
 

# User input in Python

user_input = input("Enter your name: ")
print("Hello, " +user_input + "!")


# Python built-in functions len(), type(), str(), int(), float(), bool()

#len() -> returns the length of a string
print("Length of string: ", len("John Smith")) # output: 10, whitespace included as a character

#type() -> returns the data type of a variable
print("Data type of variable: ", type(30.5)) #outpu: <class 'float'>

# str() -> converts a variable to a string
print("Convert to string: ", str(10)) # output: '10'

# int() -> converts a variable to an integer
print("Convert to integer: ", int(10.5)) # output: 10

# float() -> converts a variable to a float
print("Convert to float: ", float(10)) # output: 10.0

# bool() -> converts a variable to a boolean
print("Convert to boolean: ", bool(1)) # output: True


