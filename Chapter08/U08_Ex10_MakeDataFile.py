from random import randint

def main():
    '''
    Creates data file for U08_Ex10_FuelEconomy2.py
    Starting odometer reading is 10000.
    Ten legs of a journey are created.
    Miles for each leg vary between 300 and 500 miles.
    Fuel economy for each leg varies between 18 and 32 mpg.
    :return: None
    '''
    dataFile = open('U08_Ex10_DataFile.txt', 'w')
    dataFile.write('10000\n')
    odo = 10000
    for i in range(10):
        miles = randint(300, 500)
        mpg = randint(18, 32)
        odo += miles
        fuel = int(miles / mpg)
        dataFile.write(str(odo) + ' ' + str(fuel) + '\n')
    dataFile.close()

main()