'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
sentence1=input('give me a sentence about your favorite sport: ')

list1=sentence1.split()

most_common=(max(set(list1)))

print(most_common)


