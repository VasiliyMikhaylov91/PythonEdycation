def fibonacci(number, first=1, second=1):
    if number == 1 or number == 2:
        return second
    else:
        return fibonacci(number - 1, second, first + second)


for i in range(1, 6):
    print(fibonacci(i))
