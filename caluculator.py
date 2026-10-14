def add(a, b):
    return a+b


def sub(a, b):
    pass


def mul(a, b):
    pass


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b