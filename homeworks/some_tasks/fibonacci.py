def fibonacci(number, first=1, second=1):
    return second if number == 1 or number == 2 else fibonacci(number - 1, second, first + second)


for i in range(1, 56):
    print(fibonacci(i))
