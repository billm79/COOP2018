# from U09_S00_Racquetball import gameOver, simOneGame, simNGames
from U09_Ex01_RacquetballBestOfN import matchOver, simOneMatch, simNMatches

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
    results.append(runTest('gameOver(5, 8)', False))
    results.append(runTest('gameOver(14, 4)', False))
    results.append(runTest('gameOver(4, 14)', False))
    results.append(runTest('gameOver(15, 4)', True))
    results.append(runTest('gameOver(4, 15)', True))
    printResults(results)

def testSimOneGame():
    results = []
    results.append(runTest('simOneGame(.3, .35)', 'null'))
    results.append(runTest('simOneGame(.3, .35)', 'null'))
    results.append(runTest('simOneGame(.3, .35)', 'null'))
    printResults(results)

def testSimNGames():
    results = []
    results.append(runTest('simNGames(500, .5, .5)', 'null'))
    results.append(runTest('simNGames(500, .35, .3)', 'null'))
    results.append(runTest('simNGames(500, .3, .35)', 'null'))
    results.append(runTest('simNGames(500, .6, .65)', 'null'))
    results.append(runTest('simNGames(500, .3, .6)', 'null'))
    results.append(runTest('simNGames(500, .1, .9)', 'null'))
    printResults(results)

def testMatchOver():
    results = []
    results.append(runTest('matchOver(5, 0, 0)', False))
    results.append(runTest('matchOver(5, 0, 1)', False))
    results.append(runTest('matchOver(5, 0, 2)', False))
    results.append(runTest('matchOver(5, 0, 3)', True))
    results.append(runTest('matchOver(5, 0, 4)', True))
    results.append(runTest('matchOver(5, 1, 1)', False))
    results.append(runTest('matchOver(5, 1, 2)', False))
    results.append(runTest('matchOver(5, 1, 3)', True))
    results.append(runTest('matchOver(5, 2, 2)', False))
    results.append(runTest('matchOver(5, 3, 2)', True))
    results.append(runTest('matchOver(11, 6, 2)', True))
    results.append(runTest('matchOver(11, 3, 2)', False))
    printResults(results)

def testSimOneMatch():
    results = []
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .5, .5)', 'null'))
    results.append(runTest('simOneMatch(5, .35, .3)', 'null'))
    results.append(runTest('simOneMatch(5, .35, .3)', 'null'))
    results.append(runTest('simOneMatch(5, .35, .3)', 'null'))
    results.append(runTest('simOneMatch(5, .35, .3)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .35)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .35)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .35)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .35)', 'null'))
    results.append(runTest('simOneMatch(5, .6, .65)', 'null'))
    results.append(runTest('simOneMatch(5, .6, .65)', 'null'))
    results.append(runTest('simOneMatch(5, .6, .65)', 'null'))
    results.append(runTest('simOneMatch(5, .6, .65)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .6)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .6)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .6)', 'null'))
    results.append(runTest('simOneMatch(5, .3, .6)', 'null'))
    printResults(results)

def testSimNMatches():
    results = []
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    results.append(runTest('simNMatches(500, 5, .3, .35)', 'null'))
    printResults(results)


if __name__ == '__main__':
    testSimNMatches()
