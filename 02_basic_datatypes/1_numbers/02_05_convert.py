'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
example= 6
x= float(example)
y= int(example)
print(x)
print(y)

floor= 6//4.5
print(floor)

val1=input("Give me a number between 1 and 10: ")
val2=input("Give me another number between 1 and 10: ")
val3=int(val1)*int(val2)
print(val3)

