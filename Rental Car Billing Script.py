
#ATTENTION USERS!
# Requires input!
#1st. Budget, Daily, or Weekly rental - Type D, B, or W
#2nd. Enter a number indicating length of time to rent car..ex 5 (for 5 days or weeks)
#3rd. Enter car's starting mileage
#4th. Enter car's ending mileage

#User input here
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
#have to convert user input to int to use in later formula
if rentalCode =='B':
    rentalPeriod = int(input('Number of Days rented:\n'))
elif rentalCode =='D':
    rentalPeriod = int(input('Number of Days rented:\n'))
elif rentalCode =='W':
    rentalPeriod = int(input('Number of Weeks rented:\n'))
#the base charges for each of the user input selections
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00

#user input for starting odometer reading and the final odometer reading when they are one renting the car
odoStart = input('Starting Odometer Reading:\n')

odoEnd = input('Ending Odometer Reading:\n')

#second use of branching using if, and elifx2
#adds charges based on length of time
if rentalCode =='B':
  baseCharge = int(rentalPeriod) * int(budgetCharge)
elif rentalCode =='D':
  baseCharge = int(rentalPeriod) * int(dailyCharge)
elif rentalCode =='W':
  baseCharge = int(rentalPeriod) * int(weeklyCharge)




#calculates total miles driven based on user input
totalMiles = int(odoEnd) - int(odoStart)
#base milecharge for the formulas (also the missing piece from my first draft)
mileCharge = float(totalMiles * 0.25)

#third use of branching using nested conditions
#Adds charges based on mileage
if rentalCode == 'B':
    mileCharge = float(totalMiles * 0.25)
#if the driver drives less than or equal to 100 miles daily, there will be no additional costs
#else the drive does drive more than 100 miles a day, the milecharge kicks in
elif rentalCode == 'D':
    averageDayMiles = float(totalMiles)/float(rentalPeriod)
    if float(averageDayMiles) <= 100:
        totalCharge = baseCharge
    else:
        extraMiles = float(averageDayMiles) - 100
        mileCharge = 0.25 * float(extraMiles)
#if weekly mileage is less than or equal to 900 miles, there will be no additional costs
#else there will be an additional charge of $100 per week the vehical is rented
elif rentalCode == 'W':
    averageWeekMiles = totalMiles / rentalPeriod
    if averageWeekMiles <= 900:
        totalCharge = baseCharge
    else:
        mileCharge = baseCharge + float(rentalPeriod * 100)

amtDue = float(baseCharge) + float(mileCharge)

#Summary read out 
print('Rental Summary')
print('Rental Code:   ' + str(rentalCode))
print('Rental Period:   ' + str(rentalPeriod))
print('Starting Odometer:   ' + str(odoStart))
print('Ending Odometer:   ' + str(odoEnd))
print('Miles Driven:    ' + str(totalMiles))
print('Amount Due:      ' + '$' + str('%.2f' % amtDue))
