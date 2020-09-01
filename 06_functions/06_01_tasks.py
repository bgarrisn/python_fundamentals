'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def division1(x):
    if x%7==0 or x%4==0:
        return True
    else:
        return False

def division2(x):
    if x%4==0 and x%7==0:
        return True
    else:
        return False

number=input("give me a number between 1 and 1,000,000,000: ")


var1=division1(int(number))
var2=division2(int(number))

print(var1)
print(var2)