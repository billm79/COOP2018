# U09_Ex05_VBComp.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 15 Dec 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#   Compares non-rally-scoring (old school) volleyball to modern rally scoring volleyball
#
# Algorithm (pseudocode)
#   introduce program
#   get input (probA, probB, numGames)
#   simulate games (by calling simNMatches from U09_Ex03_Volleyball and U09_Ex04_VolleyballRally)
#   print report
#
#   INPUT
#       probabilities that teams A and B will win when serving (pSrvA, pSrvB)
#       number of matches to play (numMatches)
#
#   OUTPUT
#       Games simulated: ###
#
#       Scoring     Wins A  Wins B  Wins Diff  Pctg A  Pctg B  Pctg Diff
#       ----------  ------  ------  ---------  ------  ------  ---------
#       Non-Rally   ######  ######     ######  ###.#%  ###.#%     ###.#%
#       Rally       ######  ######     ######  ###.#%  ###.#%     ###.#%
#
#       Interpretation: Rally scoring magnifies/reduces/has no effect on the relative advantage enjoyed by the better team.


from U09_Ex03_Volleyball import simNMatches as simNMatchesNR
from U09_Ex04_VolleyballRally import simNMatches as simNMatchesR
from U09_Ex04_VolleyballRally import getInput

def main():
    introProg()
    probA, probB, numMatches = getInput()
    quitVal = ''
    while not quitVal:
        matchesANR, matchesBNR = simNMatchesNR(probA, probB, numMatches)
        matchesAR, matchesBR = simNMatchesR(probA, probB, numMatches)
        printReport(probA, probB, matchesANR, matchesBNR, matchesAR, matchesBR)
        quitVal = input("\nPress Return to repeat; type 'q' and press Return to quit. ")

def introProg():
    print('\nThis program compares non-rally scoring (old school) to modern rally scoring in the game of volleyball.')
    input('(press Return to continue)')

def printReport(probA, probB, mAnr, mBnr, mAr, mBr):
    mNR = mAnr + mBnr; mR = mAr + mBr
    pAnr = mAnr / mNR; pBnr = mBnr / mNR
    pAr = mAr / mR; pBr = mBr / mR
    diffWinsNR = abs(mAnr - mBnr); diffPctgNR = abs(pAnr - pBnr)
    diffWinsR = abs(mAr - mBr); diffPctgR = abs(pAr - pBr)
    compPctg = diffPctgR - diffPctgNR
    diffProbs = abs(probA - probB)
    print('')
    print('Games simulated {}\t\tProbability difference: {:.1%}'.format(mAr + mBr, diffProbs))
    print('')
    print('Scoring     Wins A  Wins B  Wins Diff  Pctg A  Pctg B  Pctg Diff')
    print('----------  ------  ------  ---------  ------  ------  ---------')
    print('{:<9}  {:>6}  {:>6}     {:>6}  {:>6.1%}  {:>6.1%}     {:>6.1%}'.
          format('Non-Rally', mAnr, mBnr, diffWinsNR, pAnr, pBnr, diffPctgNR))
    print('{:<9}  {:>6}  {:>6}     {:>6}  {:>6.1%}  {:>6.1%}     {:>6.1%}'.
          format('Rally', mAr, mBr, diffWinsR, pAr, pBr, diffPctgR))
    print('\nInterpretation: Rally scoring {} the relative \nadvantage enjoyed by the better team.'.
          format('MAGNIFIES' if compPctg > diffProbs else 'REDUCES' if compPctg < -1 * diffProbs else 'has NO EFFECT on'))

if __name__ == '__main__':
    main()