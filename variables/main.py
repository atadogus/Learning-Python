from fractions import Fraction
import math

# help(Fraction)

print(Fraction(2))  # when a second value is not written, the denominator is automatically equal to 1

print(Fraction(denominator=2, numerator=1))

print(Fraction(2, 1))  # when not specified, the first value is numerator and the second is denominator

print(Fraction(1, 2))

print(Fraction("2/3"))  # python can parse a string when written in this format and return a fraction

print(Fraction(2, 3) + Fraction(3, 4))

print(Fraction(3, 5).numerator)

print(Fraction(3.14).limit_denominator(22))  # constrains the max denominator that the fraction can return

print(Fraction(0.125))  # floats can be represented as fractions since they are finite

print(Fraction(math.pi))  # closest representation of the irrational number since the computer can contain these numbers as rationals
print(Fraction(math.e))
print(Fraction(math.sqrt(2)))

print(Fraction(0.3))
print(format(0.3, "0.25f"))  # python actually does not store the floating value 0.3 as 0.300000000.... but as the number
# which is printed out, that is why the result of the fraction is not 3/10 but some weird stuff

# note: format(floating number, significant digits) returns the number with the amount of significant digits specified
# in the format
