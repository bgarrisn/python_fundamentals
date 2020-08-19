'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''

num1=1
num2=50

squares=[]
for num in range(num1, num2+1):
    square=num**2
    squares.append(square)

print(squares)
