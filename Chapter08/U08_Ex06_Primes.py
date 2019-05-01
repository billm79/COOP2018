# U08_Ex06_Primes.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Finds every prime number less than or equal to a given number.
#   Uses is_prime() from U08_Ex05_isPrime.py
#
# Algorithm (pseudocode)
#   introduce program
#   get integer number from user
#   loop from 2 to given number
#       call is_prime() to test for primeness
#       if prime, print


from U08_Ex05_isPrime import is_prime

def main1():
    # introduce program
    print('This program prints all prime numbers up to a given number.\n')

    # get integer number from user
    num = int(input('Enter an integer: '))

    # loop from 2 to given number
    thisNum = 2
    print('Primes: ', end='')
    firstTime = True
    while thisNum <= num:
        # call is_prime() to test for primeness
        # if prime, print
        if is_prime(thisNum):
            if firstTime:
                print('{}'.format(thisNum), end='')
                firstTime = False
            else:
                print(', {}'.format(thisNum), end='')
        thisNum += 1
    print()

def primes_list(num):
    # int num is argument

    # loop from 2 to given number
    thisNum = 2
    primes = []
    while thisNum <= num:
        # call is_prime() to test for primeness
        # if prime, add to primes
        if is_prime(thisNum):
            primes.append(thisNum)
        thisNum += 1
    return primes


def main2():
    # introduce program
    print('This program prints all prime numbers up to a given number.\n')

    # get integer number from user
    num = int(input('Enter an integer: '))

    # call primes_list(), setting return value to primes[]
    primes = primes_list(num)

    # print list returned by prime_list()
    print('Primes: ', end='')

    for prime in primes:
        print('{} '.format(prime), end='')
    print()


def main3():
    # introduce program
    print('\nThis program uses the sieve of Eratosthenes to print all prime numbers up to a given number.\n')

    # get integer number from user
    num = int(input('Enter an integer: '))

    # initialize a list the length of num + 1
    # set all elements in primes to True
    print("\nInitializing list...")
    primes = [True] * (num + 1)

    # set all multiples of prime numbers in primes[] to False, starting at the first prime number, 2
    print("Eliminating non-primes...")
    count = 0
    dots = 0
    for i in range(2, int(len(primes) / 2)):
        for j in range(i * 2, len(primes), i):
            primes[j] = False
            # count += 1
            # if count % 30000 == 0:
            #     print('.', end='')
            #     dots += 1
            #     if dots % 120 == 0:
            #         print()
    print()

    # print all primes (elements in primes[] with value of True)
    count = 0
    print('\nPrime numbers <= {}: '.format(num))
    for i in range(2, len(primes)):
        if primes[i]:
            print('{} '.format(i), end='')
            count += 1
            if count % 15 == 0:
                print()
    print()


if __name__ == '__main__':
    main3()
