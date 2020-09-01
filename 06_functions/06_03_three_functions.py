'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def fun1(x):
    if fun2(y)==1:
        return True
    else:
        return False

def fun2(y):
    if fun1(x)==1:
        return True
    else:
        return False

def fun3(z):
    if fun2(y) and fun1(x)==1:
        return True
    else:
        return False

x=input("give me a number between 1 and 10: ")
y=input("give me a number between 1 and 10: ")
z=input("give me a number between 1 and 10: ")

answer1=fun1(int(x))
answer2=fun2(int(y))
answer3=fun3(int(z))

print(answer1)
print(answer2)
print(answer3)