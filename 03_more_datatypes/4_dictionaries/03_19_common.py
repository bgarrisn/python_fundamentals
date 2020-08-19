'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''


dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}



result={}

for key in dict_1:
    if key in dict_2:
        result[key] = dict_2[key] + dict_1[key]
    else:
        result[key]=dict_1[key]
for key in dict_2:
    if key not in dict_1:
        result[key]=dict_2[key]

result.update(dict_1)

print(result)


#a={(1, 2):5}

#randlist=['a', 1, 4, 'd', 5, 9, 'e', 'f', 8, 3]

#for i, value in enumerate(randlist):
    #if value=='d':
       # print(i)
       # break
   # else:
     #   print("Sorry not here.")
