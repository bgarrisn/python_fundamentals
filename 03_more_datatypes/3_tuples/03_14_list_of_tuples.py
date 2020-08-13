'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''


sentence2=input('Give me a sentence: ')

list1 = sentence2.split()



words=[]
for word in list1:
    letters_list=[]
    for letter in word:
        letters_list.append(letter)
    letters_tuple=tuple(letters_list)
    words.append(letters_tuple)

print(words)
