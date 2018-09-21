# U08_Ex02_Windchill.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 2
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Prints a table of windchill values.
#       Rows->windspeed 0-50mph, step 5.
#       Columns->-20°F – 60°F, step 10.
#   
#   Formula: windchill = 35.74 + (0.6215)T - (35.75)V^0.16 + (0.4275)TV^0.16
#
# Algorithm (pseudocode)
#   introduce program
#   print table title
#   print table headings with dashed lines below for each column
#   loop on windspeed, 0-50, inclusive
#       print windspeed in first column (integer value)
#       loop on temperature, -20°F–60°F, inclusive
#           print windchill for given windspeed (outer loop) and temp (inner loop) (integer value)
#
#   windchill:
#       temp and velocity are arguments
#       return result of windchill formula: windchill = 35.74 + (0.6215)T - (35.75)V^0.16 + (0.4275)TV^0.16


def windchill(vel, temp):
    '''
    Calculates windchill from temperature and velocity.
    Formula: windchill = 35.74 + (0.6215)temp - (35.75)vel^0.16 + (0.4275)temp(vel^0.16)
    :param temp: float temperature
    :param vel: float velocity
    :return: float windchill
    '''
    return 35.74 + 0.6215 * temp - 35.75 * vel**0.16 + 0.4275 * temp * vel**0.16

def main():
    # introduce program
    print('\nThis program prints a table of windchill values for windspeeds from 0mph to 50mph and temperatures from -20°F to 60°F.')

    # print table title
    print('\n\nWindchill for Various Combinations of Windspeed and Temperature\n')

    # print table headings with dashed lines below for each column
    print('{}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}'
          .format('Windspeed, (mph)', '-20°F', '-10°F', '0°F', '10°F', '20°F', '30°F', '40°F', '50°F', '60°F'))
    print('----------------\t-----\t-----\t-----\t-----\t-----\t-----\t-----\t-----\t-----')
    # loop on windspeed, 0-50, inclusive
    for vel in range(0, 51, 5):
        # print windspeed in first column (integer value)
        print('{:^16}'.format(vel), end='')
        # loop on temperature, -20°F–60°F, inclusive
        for temp in range(-20, 61, 10):
            # print windchill for given windspeed (outer loop) and temp (inner loop) (integer value)
            print('\t{:>5.0f}'.format(windchill(vel, temp)), end='')
        print()

if __name__ == '__main__':
    main()
