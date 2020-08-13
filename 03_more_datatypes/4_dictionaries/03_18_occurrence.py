'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
word1=input('give me a word: ')

freq_word = {}

for i in word1:
    if i in freq_word:
        freq_word[i] += 1
    else:
        freq_word[i] = 1

print(freq_word)