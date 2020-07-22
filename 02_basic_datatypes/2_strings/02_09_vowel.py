'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
user=input("Write a sentence: ")
a=user.count("a")
e=user.count("e")
i=user.count("i")
o=user.count("o")
u=user.count("u")

print(a+e+i+o+u)

#this "solves" the challenge but I am sure it is not the best way to do it
print("a is equal to: " + str(a))
print("e is equal to: " + str(e))
print("i is equal to: " + str(i))
print("o is equal to: " + str(o))
print("u is equal to: " + str(u))






