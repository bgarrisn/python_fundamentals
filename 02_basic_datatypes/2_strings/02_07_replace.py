'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

user=input("Tell me what you would like to do today: ")
symbol=input("What is your favorite symbol on the keyboard? ")

print(user.replace(user[0], symbol))