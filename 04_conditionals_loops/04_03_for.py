'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

num1=1
num2=100

for num in range(num1, num2+1):
    if num %2!=0:
        print(num)
