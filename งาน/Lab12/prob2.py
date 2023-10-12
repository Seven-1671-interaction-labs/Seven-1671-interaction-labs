def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
