'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  maxval = max(list)
  print(maxval)

  minval = min(list)
  print(minval)

  averageval = int(sum(list)/len(list))
  print(averageval)

  sumval= sum(list)
  return sumval




# call the function below here

numbers=stats(example_list)

print(numbers)