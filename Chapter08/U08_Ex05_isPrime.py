# U08_Ex05_isPrime.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Determines if a given number is prime using a function called is_prime()
#
# Algorithm (pseudocode)
#   introduce program
#   get integer (num) from user
#   call is_prime() which determines if num is prime
#   print results
#
#   is_prime:
#       integer num is argument
#       loop from 2 to int(sqrt(num))
#           if num is evenly divided by loop variable, return False
#       return True


from math import sqrt

def is_prime(num):
    '''
    Determines if num is prime
    :param num: int
    :return: True if prime, False if not
    '''
    # loop from 2 to int(sqrt(num))
    div = 2
    while div <= sqrt(num):
        # if num is evenly divided by loop variable, return False
        if num % div == 0: return False
        div += 1
    # return True
    return True

def main():
    # introduce program
    print('This program determines if an integer input by the user is prime.\n')

    # get integer (num) from user
    num = int(input('Enter an integer to test for primeness: '))

    # call is_prime() which determines if num is prime
    # print results
    print('The number {} is {}a prime nubmer.'.format(num, '' if is_prime(num) else 'not '))

if __name__ == '__main__':
    main()