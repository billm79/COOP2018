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


import traceback, sys

# from _path_to_my_program_file_ import *

COLOR_BLUE = '\x1b[1;34m'
COLOR_RED  = '\x1b[6;31m'
COLOR_OFF  = '\x1b[0m'


def runTest(testStr, answer):
    """
    DO NOT CHANGE THIS FUNCTION
    Evaluates (runs) testStr (your function in your program, with parameters); records result; tests validity of result
    :param testStr: str -> the call to your function in your program
    :param answer: any type -> the correct answer your function should return
    :return: list -> [testStr, answer, actual result from your function, correctness of your result]
    """
    tb = ''     # traceback info
    try:
        result = eval(testStr)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        result = 'ERROR: ' + str(e)
        tb = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
    return [testStr, answer, result, (result == answer) if answer != 'null' else 'n/a', tb]

def printResults(results):
    """
    DO NOT CHANGE THIS FUNCTION
    Prints results
    :param results: list -> returned by runTest()
    :return: None
    """
    maxLen = [0, 0, 0, 0, 0]        # max lengths of output fields
    for i in range(len(results)):
        # determine lengths of fields based on data type
        for j in range(len(results[i])):
            thisType = type(results[i][j])
            # print(results[i][j], thisType)
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
    # print(results)        # debug
    # print(maxLen)         # debug

    # add 2 to each element of maxLen
    for i in range(len(maxLen)):
        maxLen[i] += 2

    # print results
    print('\nRESULTS:\n========')
    for result in results:
        print("{0:{4}} --> {1:>{5}} | {2:>{6}} | [ {3} ]".
              format(result[0], result[1], result[2], COLOR_BLUE + "Pass" + COLOR_OFF if result[3] else COLOR_RED + "FAIL" + COLOR_OFF,
                     maxLen[0], maxLen[1], maxLen[2]))

        # if error occured, print traceback
        if result[4]:
            for line in eval(result[4]):
                print('{}    {}{}'.format(COLOR_RED, line, COLOR_OFF), end='')
    print('========')

def testTemplate():
    results = []        # list to hold tests

    # replace   'function(params)' with str version of call to function to test (in quotes);
    #           'expected results (properly typed)' with expected results (doesn't have to be str;
    #               should be correct data type)
    # copy line multiple times to run multiple tests (with different parameters)
    results.append(runTest('function(params)', 'expected results (properly typed)'))
    printResults(results)


if __name__ == '__main__':
    # Replace 'function_to_call' with the name of the function you created above
    # function_to_call()
