# testCode.py
#
#  Author: Bill Montana
#    Date: 29 Nov 2017
#     IDE: PyCharm Community Edition
#
# Program Description
#   This tests functions written in other programs. The function must not print. It must return a single value.
#   The value can be of any type, including lists containing multiple values of differing types. So, if your
#   function needs to return multiple values, put them in a list or tuple.
#
# How to use
#   • Import the function to be tested from your program file
#   • Copy/paste testTemplate()
#   • Edit the copy
#       • change its name
#       • change the results.append... line to refer to your function in your program. Include necessary parameters.
#       • change the expected result
#       • copy/paste the results.append... line several times, once for each case you want to test.
#       • edit the parameters and expected result for each case.
#   change the function_to_call at the bottom to the test function you created here
#   run this program


from Chapter11.U11_Ex05_ListOperations import *
from Chapter11.U11_Ex07_InnerProd import *


def runTest(testStr, answer):
    """
    Don't change this function
    Evaluates (runs) testStr (your function in your program, with parameters); records result; tests validity of result
    :param testStr: str -> the call to your function in your program
    :param answer: any type -> the correct answer your function should return
    :return: list -> [testStr, answer, actual result from your function, correctness of your result]
    """
    try:
        result = eval(testStr)
    except Exception as e:
        result = 'ERROR: ' + str(e)
    return [testStr, answer, result, (result == answer) if answer != 'null' else 'n/a']

def printResults(results):
    """
    Don't change this function
    Prints results
    :param results: list -> returned by runTest()
    :return: None
    """
    maxLen = [0, 0, 0, 0]
    for i in range(len(results)):
        for j in range(len(results[i])):
            thisType = type(results[i][j])
            if thisType == str:
                thisLen = len(results[i][j])
            elif thisType == int or thisType == float:
                thisLen = len(str(results[i][j]))
            elif thisType == bool:
                thisLen = 5
            elif thisType == tuple:
                results[i][j] = str(results[i][j])
                thisLen = len(results[i][j])
            elif thisType == list:
                results[i][j] = str(results[i][j])
                thisLen = len(results[i][j])

            if thisLen > maxLen[j]:
                maxLen[j] = thisLen
    print(results)
    print(maxLen)
    for i in range(len(maxLen)):
        maxLen[i] += 2

    print('\nRESULTS:\n========')
    for result in results:
        print("{0:{4}} --> {1:>{5}} | {2:>{6}} | [ {3} ]".
              format(result[0], result[1], result[2], "Pass" if result[3] else "FAIL",
                     maxLen[0], maxLen[1], maxLen[2]))
    print('========')

def testTemplate():
    results = []
    results.append(runTest('function(params)', 'expected results (properly typed)'))
    printResults(results)


def testCount():
    results = []
    results.append(runTest('count([], 2)', 0))
    results.append(runTest('count([1,2,3], 2)', 1))
    results.append(runTest('count([1,1,3,4], 2)', 0))
    results.append(runTest('count([1,2,3,2,4,2,5,2], 2)', 4))
    printResults(results)


def testIsin():
    results = []
    results.append(runTest('isin([], 2)', 0))
    results.append(runTest('isin([1,2,3], 2)', 1))
    results.append(runTest('isin([1,1,3,4], 2)', 0))
    results.append(runTest('isin([1,2,3,2,4,2,5,2], 2)', 1))
    printResults(results)


def testIndex():
    results = []
    results.append(runTest('index([], 2)', -1))
    results.append(runTest('index([1,2,3], 2)', 1))
    results.append(runTest('index([1,1,3,4], 2)', -1))
    results.append(runTest('index([1,2,3,2,4,2,5,2], 2)', 1))
    results.append(runTest('index([1,3,3,5,4,7,5,2], 2)', 7))
    printResults(results)


def testReverse():
    results = []
    results.append(runTest('reverse([0,1,2,3,4,5,6,7,8,9])', [9,8,7,6,5,4,3,2,1,0]))
    results.append(runTest('reverse([3,2,1])', [1,2,3]))
    results.append(runTest('reverse([7,7,3,4])', [4,3,7,7]))
    printResults(results)


def testSort():
    results = []
    results.append(runTest('sort([44,88,22,33,11,99,77,66,55])', [11,22,33,44,55,66,77,88,99]))
    printResults(results)


def testInnerProd():
    results = []
    results.append(runTest('innerProd([1,2,3], [4,5,6])', 32))
    results.append(runTest('innerProd([1,2,3], [4,5])', 'Lists must be of same length.'))
    results.append(runTest('innerProd([1,2], [4,5,6])', 'Lists must be of same length.'))
    results.append(runTest('innerProd([], [4,5,6])', 'Lists must be of same length.'))
    results.append(runTest('innerProd([1,2,3], [])', 'Lists must be of same length.'))
    printResults(results)


if __name__ == '__main__':
    # Replace 'function_to_call' with the name of the function you created above
    testCount()
    testIsin()
    testIndex()
    testReverse()
    testSort()
