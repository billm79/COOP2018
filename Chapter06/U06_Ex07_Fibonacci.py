# U06_Ex07_Fibonacci.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Solve PE 3.16 using function nthFibonacci()
#   Computes the nth Fibonacci number in the classic sequence
#
# Algorithm (pseudocode)
#   introduce program
#   get n from user
#   call nthFibonacci() with n as parameter; assign result to nthFib
#   print results
#
#   nthFibonacci():
#       n is argument
#       create fibSeq = [1,1]
#       loop n-2 times
#           next number in sequence is sum of previous two; add this to list
#       return last element of list
#
#   ordSuffix(): (extra)
#       n (int) is argument
#       convert n to string in nStr var
#       create suffixList = ['st', 'nd', 'rd']
#       if last character of nStr is 1, 2, or 3 AND last two is not in the teens
#           return matching suffix from suffixList
#       otherwise return 'th'
#
#   contains(): (extra, needed by ordSuffix())
#       nStr and string are arguments
#       loop through string
#           if an element of string == nStr, return true
#       otherwise return false


def main():
    # introduce program
    print('\nThis program computes the nth Fibonacci number in the classic sequence.')

    # get n from user
    n = int(input('\nWhich term in the classic Fibonacci sequence would you like to compute? '))

    # call nthFibonacci() with n as parameter; assign result to nthFib
    nthFib = nthFibonacci(n)

    # print results
    print('\nThe {0}{1} term in the classic Fibonacci sequence is {2}.'.format(n, ordSuffix(n), nthFib))

# nthFibonacci():
#     n is argument
def nthFibonacci(n):
    # create fibSeq = [1,1]
    fibSeq = [1, 1]

    # loop n-2 times
    for i in range(2, n):
        # next number in sequence is sum of previous two; add this to list
        fibSeq.append(fibSeq[i-2] + fibSeq[i-1])
    # return last element of list
    return fibSeq[-1]

# ordSuffix(): (extra)
#     n (int) is argument
def ordSuffix(n):
    # convert n to string in nStr var
    nStr = str(n)

    # create suffixList = ['st', 'nd', 'rd']
    suffixList = ['st', 'nd', 'rd']

    # if last character of nStr is 1, 2, or 3 AND last two is not in the teens
    '''
        NOTE: These lines were used for debugging...
        print('nStr[-1] =', nStr[-1])
        print('contains(nStr[-1], "123")? ', contains(nStr[-1], '123'))
        print('n > 10?', n > 10)
        if n > 9:
            print('nStr[-2] =', nStr[-2])
        print('IF:', contains(nStr[-1], '123') and not (n > 10 and nStr[-2] == '1'))
    '''
    if contains(nStr[-1], '123') and not (n > 10 and nStr[-2] == '1'):
        # return matching suffix from suffixList
        return suffixList[int(nStr[-1])-1]
    # otherwise return 'th'
    else:
        return 'th'

# contains(): (extra, needed by ordSuffix())
#     nStr and string are arguments
def contains(nStr, string):
    # loop through string
    for char in string:
        # if an element of string == nStr, return true
        if char == nStr:
            return True
    # otherwise return false
    return False

if __name__ == '__main__':
    main()