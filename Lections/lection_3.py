# def f(x):
#     return x ** 2

# g =f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def calc1(x):
#     return x + 10

# print(calc1(10))

# def calc2(x):
#     return x * 10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
###########################################

# def sum (x, y):
#     return x + y

# sum = lambda x, y: x+y

# def mult (x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a,b))
#     # return op(a,b)

# calc(lambda x, y: x+y, 4, 5)

###########################################

# list = []

# for i in range(1, 101):
#     # if i % 2 == 0:
#     list.append(i)

# print (list)

def calc(op, x):
    return op(x)


with open('some_file.txt', 'r') as sf:
    print(list((calc(lambda x: (x, x ** 2), i) for i in map(int,sf.read().split()) if not i % 2)))