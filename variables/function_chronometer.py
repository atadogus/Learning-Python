import sys
import time

the_list = []

the = sys.intern("the")
the_list.append(the)

The = "the"
the_list.append(The)

another_the = "the"
the_list.append(another_the)

# this above method which is in the system module allows us to intern string that we pass through the method to create
# a singleton of it. In most cases, the use of this function is not required unless data optimisation and memory saving
# is required to speed up the process

# In python integers from -5 to 256 are interned and thus whenever a variable is created which points to some integer
# within this range, that pointer will be aimed at a singleton instance

print(The is another_the)

for word in the_list:
    print(hex(id(word)))

# is operator is a faster working operator for it compares the memory address of the two objects which they are pointing
# at and returns whether they point at the same memory address or not, whereas == operator, for example used for
# comparing two string, runs through both strings completely and compares each character value with the other and after,
# parsing them, gives the result


def compare_equals(n):
    first = "my string here babe, hope they are not pointing at the same thing" * 200
    second = "my string here babe, hope they are not pointing at the same thing" * 200

    for i in range(n):
        if first == second:
            pass


def compare_identity(n):
    first = sys.intern("my new string here babe, hope they are pointing at the same thing" * 200)
    second = "my new string here babe, hope they are pointing at the same thing" * 200

    for i in range(n):
        if first is second:
            pass


def time_to_execute_function(test_func):
    """Calculates the amount of time for the given function to finish executing"""

    start = time.perf_counter()
    test_func()
    end = time.perf_counter()

    return end - start


def quotient_calc(dividend: int, divisor: int):
    """Calculates quotient"""

    try:
        quotient = 0

        if divisor > 0:
            while abs(dividend) > divisor:

                if dividend < 0:
                    dividend += divisor
                    quotient -= 1

                else:
                    dividend -= divisor
                    quotient += 1

        elif divisor == 0:
            return

        else:
            while abs(dividend) > abs(divisor):

                if dividend < 0:
                    dividend -= divisor
                    quotient += 1

                else:
                    dividend += divisor
                    quotient -= 1

        return quotient

    except ZeroDivisionError:
        raise Exception("0 cannot be a divisor")


# print(f"The time it took for the '==' operation to finish executing: {time_to_execute_function(lambda: compare_equals(10000000))}")

# print(f"The time it took for the 'is' operation to finish executing: {time_to_execute_function(lambda: compare_identity(10000000))}")

# print(f"The time it took to calculate 2^10: {time_to_execute_function(lambda: 2**10)}")

# print(f"The time it took to calculate 2^10000000: {time_to_execute_function(lambda: 2**100000000)}")

# It takes more time to calculate larger numbers and working with them, since they occupy greater amounts of memory space

# print(5 // 2)

print(quotient_calc(-13, 3))