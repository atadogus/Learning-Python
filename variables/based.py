def base_representation(base: int, value: int) -> str:
    if value < 0 or base < 1:
        raise ValueError("Either the base or value is an invalid entry ")

    match base:
        case 1:
            return "0u" + "".join(str(one) for one in [1] * value + [0])

        case 2:
            return bin(value)

        case 8:
            return oct(value)

        case 10:
            return f"{value}"

        case 16:
            return hex(value)

        case base if base < 1:  # this case is to catch any values for the base that are less than or equal to 0
            raise ValueError("Base value is invalid")

        case base if base <= 36:  # "_" case represents the default

            decimal_mapping = "0123456789abcdefghijklmnopqrstuvwxyz"  # this string is for representing bases grater
            # than 10 for they will yield modular values greater than or equal to 10 which would make the reading of the
            # new representative value confusing

            decimals = []

            while value > base:  # will run the loop as long as the remaining value is greater than the base
                decimals.append(value % base)
                value = (value // base)

            decimals.append(value)  # the remaining value is the first digit of the base representation
            decimals.reverse()
            # instead of using .reverse() method, I could have used decimals.insert(0, whatever element) rather than
            # decimals.append(), the former inserts the new element at the specified location which in this case is the
            # beginning of the list and the latter adds the element at the end o the list

            # Need to reverse the order of the list, since each newly added element is placed at the end of the list.
            # Whereas the while loop finds the "something".join() method concatenates the elements of a list with what
            # is written inside "something". in between every element. For example "-".join([1, 2, 3]) would be 1-2-3
            # or ",".join([I, am, f]) would be I,am,f

            """
            result = f"Base {base}: "
            decimals = []

            while value > base:
                decimals.append(value % base)
                value = (value // base)

            decimals.append(value)
            decimals.reverse()  

            return  result + "".join(map(str, decimals))

            # this is the same as the above code         
            """

            return f"Base {base}: " + "".join([decimal_mapping[element] for element in decimals])

        case _:
            return "Can't represent it"


print(base_representation(base=16, value=2000))