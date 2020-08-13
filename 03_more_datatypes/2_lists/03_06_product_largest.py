'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
num1=input('give me a number: ')
num2=input('give me another number: ')
num3=input('give me another number: ')
num4=input('give me another number: ')
num5=input('give me another number: ')
num6=input('give me another number: ')
num7=input('give me another number: ')
num8=input('give me another number: ')
num9=input('give me another number: ')
num10=input('give me the last number: ')

number_list=[int(num1),int(num2),int(num3), int(num4),int(num5),int(num6),int(num7),int(num8),int(num9),int(num10)]

print(max(number_list))

product=1
for num in number_list:
    product*=num
    print(product)

