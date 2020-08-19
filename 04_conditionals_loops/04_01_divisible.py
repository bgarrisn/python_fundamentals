'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
num1=input('Give me a number between 1 and 1,000,000,000: ')

if int(num1) % 3==0:
    print('Look it is divisible by 3!')
else:
    print('sorry not divisible by 3')