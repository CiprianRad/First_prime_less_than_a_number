def get_natural_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            return n
        except ValueError:
            print("Inavlid input. Enter a valid integer: ")

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(2, n // 2 +1):
        if n % i == 0:
            return False
    return True

def less_prime(n):
    if n <= 2:
        return None
    else:
        n = n-1
        while is_prime(n) is False:
            n = n-1
        return n


def main():


    n = get_natural_input()
    print("The first prime number less than", n , "is", less_prime(n))


main()