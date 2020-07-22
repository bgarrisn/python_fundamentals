'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
string1=input("Give me a word: ")
string2=input("Give me another word: ")
string3=input("Give me yet another word: ")
print(str(len(string1)) + "," + string1)
print(str(len(string2)) + "," + string2)
print(str(len(string3)) + "," + string3)

