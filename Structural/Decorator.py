# TYPE 1
def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Sorry, can't divide by zero")
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(1, 2)
divide(4, 0)

print("\n")


# TYPE 2
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(message):
    print(message)


printer("Hello There")
