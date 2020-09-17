'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

def base(x):
    if int(x)> 2:
        x=x*2
        return x
    return 0


def fun1(x):
    if base(x)==1:
        return True
    return False

def fun2(y):
    if fun1(x)==1:
        return True
    return False

def fun3(z):
    if fun2(y) and fun1(x)==1:
        return True
    return False

x=input("give me a number between 1 and 10: ")
y=input("give me a number between 1 and 10: ")
z=input("give me a number between 1 and 10: ")



print(fun1(x))
print(fun2(y))
print(fun3(z))



