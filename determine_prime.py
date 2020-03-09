"""
Calculates whether a number (input on the command line) is prime
"""
import sys


def determine_prime(x):
    # Note: This is extremely slow if you plug in a prime big number
    if x < 2:
        print('Lower than 2; therefore, cannot be prime')
    else:
        print('Calculating...')
        smaller_ints = range(2, x)
        is_prime = True
        for num in smaller_ints:
            if x % num == 0:
                is_prime = False
                print(x, 'is not prime')
                break
        if is_prime is True:
            print(x, 'is prime')


def sieve_of_eratosthenes(x):
    # Note: This is extremely slow with big numbers
    if x < 2:
        print('Lower than 2; therefore, cannot be prime')
    else:
        print('Using the Sieve of Eratosthenes...')
        smaller_ints = range(2, x)
        primes = []
        composites = []
        for num in smaller_ints:
            if num not in composites:
                primes.append(num)
                for i in smaller_ints:
                    composites.append(num * i)
                    if num * (i+1) > x:
                        break
            else:
                continue
        if x in primes:
            print(x, 'is prime')
        else:
            print(x, 'is not prime')


if len(sys.argv) != 2:
    raise TypeError(f'1 argument expected; got {len(sys.argv) - 1}')

arg = sys.argv[1]
try:
    number = int(arg)
except:
    raise ValueError('Input must be an integer')

determine_prime(number)

sieve_of_eratosthenes(number)
