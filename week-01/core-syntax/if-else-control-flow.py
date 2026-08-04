''' Flow control statements can decide which
 Python instructions to execute under which conditions.

# If else statements are used to execute a block of code if a condition is true, 
and another block of code if the condition is false.  
If else statments use Comparison Operators.
Comparison operators, also called relational operators, 
compare two values and evaluate down to a single Boolean value.

'''
# relational operators

print("Equal to: ", 10 == 10) # output: True
print("Not equal to: ", 10 != 10) # output: False
print("Greater than: ", 10 > 5) # output: True
print("Less than: ", 10 < 5) # output: False
print("Greater than or equal to: ", 10 >= 10) # output: True
print("Less than or equal to: ", 10 <= 5) # output: False

# '==' is used to compare two values, 
# while '=' is used to assign a value to a variable.
# Boolean operators
''' 

TRUE, FALSE, AND, OR, NOT
TRUE and TRUE = TRUE
TRUE and FALSE = FALSE
FALSE and TRUE = FALSE
FALSE and FALSE = FALSE
TRUE or TRUE = TRUE
TRUE or FALSE = TRUE
FALSE or TRUE = TRUE
FALSE or FALSE = FALSE
NOT TRUE = FALSE
NOT FALSE = TRUE

'''

# Components of flow control statements

# flow control statements are made up of three components:
# expression or conditions that evaluate to a Boolean value (True or False)
# followed by a block of code that is executed as long as the the condition evaluates to True

# control flow statement example

# set say_it_is_opposite_day to True if today is opposite day, otherwise set it to False
today_is_opposite_day = True
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# toggle the value of say_it_is_opposite_day if today is opposite day
if say_it_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# say what day it is based on the value of say_it_is_opposite_day
if say_it_is_opposite_day == True:
    print("Today is opposite day!")
else:
    print("Today is not opposite day.")

# control flow statement demonstration with 
# nested if else statements
username = input("Enter your username: ")
if username == "admin":
    print("Welcome admin!")
    password = input("Enter your password: ")
    if password == "admin":
        print("Access granted!")
    else:
        print("Access denied!")
else:
    print("Username is unrecognized. Please try again.")







