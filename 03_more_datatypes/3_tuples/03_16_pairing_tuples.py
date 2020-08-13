'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
# save for Friday

some_list=[1, 2, 3, 4, 5, 6]

for num in some_list:
    print(num)

for num in range(0,len(some_list), 2):
    print(tuple(some_list[num: num+2]))