# *args

def summation(*args):
    # *args parameter is used for passing unlimited number of parameters through a function,
    # args name is not necessary * symbol makes the parameter limitless, *args than creates a tuple
    total = 0
    for arg in args:
        total += arg

    print(args)  # to show *args creates a tuple
    print(args[2])  # we can access each member of the args separately since args is a tuple
    return total


result = summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


# **kwargs => key word arguments


def calculate(**kwargs):
    print(kwargs)  # kwargs returns a dictionary


calculate(add=5, multiply=5, hello="hello")


def actually_calculate(n, **kwargs):
    if kwargs.get("add"):
        n += kwargs["add"]
    if kwargs.get("subtract"):
        n -= kwargs["subtract"]
    if kwargs.get("multiply"):
        n *= kwargs["multiply"]
    if kwargs.get("divide"):
        n /= kwargs["divide"]
    return n


# the .get() method is used for dictionary key search in this case to prevent the throw out of a KeyError exception since kwargs has no predefined keys
# .get() method checks whether the entered key exists or not and than acts


print(actually_calculate(n=2, subtract=2))
