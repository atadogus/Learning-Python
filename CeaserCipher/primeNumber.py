# prime number checker

def check_prime_or_not(number):
    if number == 1:
        print(f"{number} is not a prime number")
    elif number == 2:
        print(f"{number} is a prime number")
    else:
        is_prime = True
        for n in range(2, number):
            if number % n == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

check = int(input("Enter a number: "))
check_prime_or_not(check)