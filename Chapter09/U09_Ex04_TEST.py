from U09_Ex04_VolleyballRally import gameOver, simOneGame, matchOver, simOneMatch, simNMatches

def runTest(testStr, answer):
    try:
        result = eval(testStr)
    except Exception as e:
        result = 'ERROR: ' + str(e)
    return [testStr, answer, result, (result == answer) if answer != 'null' else 'n/a']

def printResults(results):
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

def testGameOver():
    results = []
    results.append(runTest('gameOver(0, 0)', False))
    results.append(runTest('gameOver(5, 10)', False))
    results.append(runTest('gameOver(25, 3)', True))
    results.append(runTest('gameOver(3, 25)', True))
    results.append(runTest('gameOver(24, 25)', False))
    results.append(runTest('gameOver(23, 25)', True))
    results.append(runTest('gameOver(29, 29)', False))
    results.append(runTest('gameOver(28, 30)', True))
    printResults(results)

def testSimOneGame():
    results = []
    results.append(runTest('simOneGame(.5, .5, "A")', 'null'))
    results.append(runTest('simOneGame(.5, .5, "A")', 'null'))
    results.append(runTest('simOneGame(.3, .3, "A")', 'null'))
    results.append(runTest('simOneGame(.3, .3, "A")', 'null'))
    results.append(runTest('simOneGame(.4, .9, "A")', 'null'))
    results.append(runTest('simOneGame(.4, .9, "A")', 'null'))
    results.append(runTest('simOneGame(.9, .4, "A")', 'null'))
    results.append(runTest('simOneGame(.9, .4, "A")', 'null'))
    results.append(runTest('simOneGame(.4, .6, "A")', 'null'))
    results.append(runTest('simOneGame(.4, .6, "A")', 'null'))
    printResults(results)

def testMatchOver():
    results = []
    results.append(runTest('matchOver(0, 0)', False))
    results.append(runTest('matchOver(1, 3)', True))
    results.append(runTest('matchOver(3, 1)', True))
    results.append(runTest('matchOver(2, 1)', False))
    results.append(runTest('matchOver(2, 3)', True))
    printResults(results)

def testSimOneMatch():
    results = []
    results.append(runTest('simOneMatch(.5, .5)', 'null'))
    results.append(runTest('simOneMatch(.5, .5)', 'null'))
    results.append(runTest('simOneMatch(.3, .3)', 'null'))
    results.append(runTest('simOneMatch(.3, .3)', 'null'))
    results.append(runTest('simOneMatch(.4, .9)', 'B'))
    results.append(runTest('simOneMatch(.4, .9)', 'B'))
    results.append(runTest('simOneMatch(.9, .4)', 'A'))
    results.append(runTest('simOneMatch(.9, .4)', 'A'))
    results.append(runTest('simOneMatch(.4, .6)', 'B'))
    results.append(runTest('simOneMatch(.4, .6)', 'B'))
    printResults(results)

def testSimNMatches():
    results = []
    results.append(runTest('simNMatches(.5, .5, 500)', 'null'))
    results.append(runTest('simNMatches(.5, .5, 500)', 'null'))
    results.append(runTest('simNMatches(.3, .3, 500)', 'null'))
    results.append(runTest('simNMatches(.3, .3, 500)', 'null'))
    results.append(runTest('simNMatches(.4, .9, 500)', 'null'))
    results.append(runTest('simNMatches(.4, .9, 500)', 'null'))
    results.append(runTest('simNMatches(.9, .4, 500)', 'null'))
    results.append(runTest('simNMatches(.9, .4, 500)', 'null'))
    results.append(runTest('simNMatches(.4, .6, 500)', 'null'))
    results.append(runTest('simNMatches(.4, .6, 500)', 'null'))
    printResults(results)


if __name__ == '__main__':
    testSimNMatches()
