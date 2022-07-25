def f(x):
    return x**2

g = f # переменная ж хранит функцию ф
# print(f(1))

# print(g(4))
# print(type(f))

def calc1(x):
    return x+10

# print(calc1(10))

def calc2(x):
    return x*10

# def math(op,x): # в качестве аргумента передается функция
    print(op(x))

# math(calc1, 10)

# def sum(x,y):
#    return x+y

# sum = lambda x,y: x+y # та же функция, что и сверху

def mylt(x,y):
    return x*y

def calc(op,a,b):
    print(op(a,b))
    # return op(a,b)

calc(lambda x,y: x+y, 4,5)