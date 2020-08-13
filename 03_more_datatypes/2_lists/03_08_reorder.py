'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

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

newlist=[number_list[1],number_list[3],number_list[5],number_list[7],number_list[9], number_list[8], number_list[7],number_list[6],number_list[4],number_list[2],number_list[0]]
print(newlist)
