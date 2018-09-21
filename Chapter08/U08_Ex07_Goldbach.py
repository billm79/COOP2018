# U08_Ex07_Goldbach.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Checks the Goldbach conjecture for numbers input by user.
#   The Goldbach conjecture asserts that every even number is the sum of two prime numbers.
#
# Algorithm (pseudocode)
#   introduce program
#   get integer number from user
#   call goldbach() with number
#   print appropriate message based on return value
#
#   goldbach:
#       integer num is argument
#       if number is even, return empty list
#       get list of primes using primes_list() from U08_Ex06_Primes.py
#       loop through list to select first number (num1)
#           loop through list again (nested) to select second number (num2)
#               if num1 + num2 equals num, return list containing num1 and num2
#       return empty list


from U08_Ex06_Primes import primes_list

def goldbach(num):
    '''
    Checks Goldbach conjecture for num.
    The Goldbach conjecture asserts that every even number is the sum of two prime numbers.
    :param num: int
    :return: -1 if num is odd; [] if no primes found; [num1, num2] if num1 + num2 == num
    '''
    # integer num is argument
    # if number is even, return empty list
    if num % 2 == 1: return -1

    # get list of primes using primes_list() from U08_Ex06_Primes.py
    primes = primes_list(num)

    # loop through list to select first number (num1)
    for num1 in primes:
        # loop through list again (nested) to select second number (num2)
        for num2 in primes:
            # if num1 + num2 equals num, return list containing num1 and num2
            if num1 + num2 == num: return [num1, num2]
    # return empty list
    return []

def main():
    # introduce program
    print('This program checks the Goldbach conjecture for a given number.\n')

    # get integer number from user
    num = int(input('Enter an integer: '))

    #   call goldbach() with number
    result = goldbach(num)

    #   print appropriate message based on return value
    if result == -1:
        print('The number you entered was odd. The Goldbach conjecture only applies to even numbers.')
    elif not result:
        print('No primes were found that add to equal {}'.format(num))
    else:
        print('{} can be expressed as the sum of these two primes: {} and {}'.format(num, result[0], result[1]))

if __name__ == '__main__':
    main()