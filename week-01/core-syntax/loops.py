'''
Loops in python are control flow statements that 
allow block of code to be executed repeatedly as long as
a condition evalutates to True. 
 Two types of loops in python While loops and for loops.

'''

# While loops : contain the following
# While keyword
# condition that evaluates to a boolean value (True or False)
# colon
# block of code to be executed repeatedly

# loop continues to execute as long as number is less than 6
# will stop executing when number is equal to 6

number = 1
while number < 6:
    print(number)
    number +=1


name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# break is a keyword used 
# to exit a loop when a certain conditon is met.


while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')


# Continue is a keyword used to skip the current iteration 
# of a loop and move on to the next iteration.

while True:
    print('Who are you?')
    name = input()
    if (name != 'Sam'):
        continue
    print('Hello, Sam. What is the password? (Hint: It is a fish.)')
    password = input()
    if password == 'tuna':
        break
print('Access Granted!.')

# for loops and the in-buitl 'range()' Function : allow execution of a 
# block of code a specific number of times.
# For keyword
# variable name to hold current value of iteration
# in keyword
# call to range() function with up to three integers passed to it
# colon

name = 'Samuel'
print ("hello")
for i in range(len(name)):
    print('Iteration ' + str(i)+' is set to ' + str(name[i]))
print('For loop has ended.')


# prints number from 5 to 9,
#  excludes the last number in the range
for i in range(5, 10):
    print(i)


# range() function with three arguments, 
# the first argument is the starting number,
# the second argument is the ending number(will be excluded)
# third argument is the amount to increment 
# on every each iteration
for i in range(1, 8, 2):
    print(i)



'''
Modules in python are files that contain python built-functions
to perform repeatitve tasks.
Examples of built-in modules in python are:
 math, random, os, sys, datetime, etc.
'''

import random

#print 5 random numbers between 1 and 100
for i in range(5):
    print(random.randint(1, 100))