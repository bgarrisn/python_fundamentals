'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
num1=input("Give me a number: ")
num2=input("Give me another number: ")

num1=int(num1)
num2=int(num2)

sumnum=[]


for i in range(num1, num2+1):
    sumnum.append(i)

print("The sum is: " + str(sum(sumnum)))