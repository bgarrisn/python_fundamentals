'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
userwords=input("type the words hello world: ")
userletter=input("pick a letter in the words above: ")
result=userwords.find(userletter)

print(result)