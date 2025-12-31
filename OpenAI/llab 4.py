a = int(input("Enter min"))
b = int(input("Enter max"))

def count_odd(a, b):
    countodd = 0
    for num in range(a, b + 1):
        if num% 2!= 0:
            countodd += 1
    print("odd count:", countodd)

    return countodd

count_odd(a, b)
def count_even(a, b):
    counteven = 0
    for num in range(a, b + 1):
        if num % 2 != 0:
            counteven += 1
    print("even count:", counteven)

    return counteven


count_even(a, b)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_prime(start, end):
    countprime = 0
    for num in range(start, end + 1):
        if is_prime(num):
            countprime += 1
    print("prime count", countprime)
    return countprime


count_prime(a, b)


