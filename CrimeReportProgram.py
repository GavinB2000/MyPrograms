""" Program iterates through a CSV file of crimes in Fairfax county 
    Made by Gavin Birk
    CrimeList.csv must be in the same folder as the program to work
    Program was made in November of 2024 in my IT 209 course
"""

# Subclass of List, creates a default name and sets local variables for default (or give name)
# The lowest day in the CrimeReport CSV file, and the highest week in the CrimeReport CSV file
class FCPDCrime(list):
    def __init__(self, name = 'Fairfax County Police Crime Report'):
        self.name = name
        self.maxWeek = 0
        self.minWeek = 0
        super().__init__()
# Creates and displays crimes based on what zip code user puts in select, default is for all zip codes
    def countByCrime(self, select = 'all'):
        # Dictionaries for the crime code and the type of crime
        crimeDict = {}
        typeOfCrime = {}
        # Displays what this class does
        print("\nList of crimes by code, sorted by frequency, for", select, 'zip code(s)\n')
        print(f"{self.name} for the week {self.minWeek}  through {self.maxWeek} \n")
    # Adds crime code to crimeDict and name of crime to typeofCrime dictionary, then get the total number of crimes
        for c in self:
            if c[1] not in crimeDict and (select == 'all' or select in c[-1]):
                crimeDict[c[1]] = 1
                typeOfCrime[c[1]] = c[2]
            elif (select == 'all' or select in c[-1]):
                crimeDict[c[1]] += 1
                typeOfCrime[c[1]] = c[2]
        sumofCrimes = sum(crimeDict.values())
    # Function found here: https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
    # Sorts dictionary in desending order
        sortedCrimes = sorted(crimeDict.items(), key = lambda item: item[1], reverse = True)
    # After sorting the crimes, percent calculates the percentage of each crime that happened, then it displays
    # On each line (ordered by number of occurances of the crime)
        for crimes, numberOfCrimes in sortedCrimes:
            percent = (numberOfCrimes / sumofCrimes) * 100
        # gets the name of the crime from the list typeOfCrime using the key crimes (crime code)
            getCrime = typeOfCrime.get(crimes)
            print(f"{crimes.ljust(12)} {str(numberOfCrimes).ljust(2)} {round(percent, 2)}% {getCrime}")
            
# Creates and returns a list of crimes for a zip code user enters in a list called zipCodeList
    def zipCodeList(self, zip = '22030'):
        zipCodeList = []
    # Appends crimes from self for the zip code, returns zipCodeList afterwards
        for c in self:
            if c[-1] not in zipCodeList and (zip == c[8]):
                zipCodeList.append(c)
        return zipCodeList
                
# Counts the percentage of crimes for all zip codes in the CrimeReports.csv file in a dictionary called zipDict
    def countByZip(self):
        zipDict = {}
        print(f"\nList of crimes by code, sorted by frequency, for all zip codes\n")
        print(f"{self.name} for the week {self.minWeek} through {self.maxWeek}\n")
    # Counts number of instances of each crime in zipDict 
        for z in self:
            if z[8] not in zipDict:
                zipDict[z[8]] = 1
            else:
                zipDict[z[8]] += 1
    # Adds the number of all crimees for all dictionaires together, then sorts the dictionary by number of crimes per zip code
        sumOfZip = sum(zipDict.values())
        sortedZip = sorted(zipDict.items(), key = lambda item: item[1], reverse=True)
    # Displays values for all zip codes
        for crimes, numberCrimes in sortedZip:
            percentOfCrimes = (numberCrimes / sumOfZip) * 100
            print(f"{crimes}  {str(numberCrimes).ljust(3)} {round(percentOfCrimes, 2)}%")
            
        
    # Opens the file CrimeReports.csv and appends to self
    def load(self, file='CrimeReports.csv'):
        o = open(file)
        lines = o.readlines()
        o.close
        for c in lines:
            splitLines = c.strip('\n').split(',')
            super().append(splitLines)
        # finds the lowest and highest calendar date in the csv file
        for c in self:
            self.minWeek = c[3]
            break
        for c in self:
            self.maxWeek = c[3]
        return len(self)

# Displays the output of all values within a row of the dictionary made from loading the CrimeReports.csv file
    def printCrimes(self, searchKey = 'all', zip = 'all', locale = 'all'):
    # Value for total number of crimes based on search criteria, makes searchKey and locale uppercase to reduce errors
        totalCrimes = 0
        searchKey = searchKey.upper()
        locale = locale.upper()
        # Displays name of program given and the week of crimes the program is for
        print("\n IT 209 - Assignment A7 \n")
        print(f"{self.name} for the week {self.minWeek} through {self.maxWeek}\n")
        # Prints the output of the self list based on what criteria is given, default prints all values
        for c in self:
            if (searchKey in c[2] or searchKey == 'ALL') and (c[8] == zip or zip == 'all') and (locale == 'ALL' or locale in c[6]):
                print(f"{c[0]} {c[1].ljust(12)} {c[2].ljust(50)} {c[3]} {c[4]} {c[5].ljust(50)} {c[6].ljust(15)} {c[7]} {c[8]}")
                totalCrimes += 1
        print(f'\n{totalCrimes} calls recorded for the search area')
                
""" GLOBAL CODE """
FC = FCPDCrime(name = 'IT209 A7 - FCPD Crime Reporting Analytics Class')
input("Test 1. Press enter to load the CrimeReports.csv file \n")
FC.load(file = 'CrimeReports.csv')
print("\nLoaded!")
input("Test 2. Press enter to print ALL crimes")
FC.printCrimes()
input("\n Press enter to test filtering crimes, starting with zip code 22030")
FC.printCrimes(zip = '22030')
input("\n Press enter to test filtering by locale Annandale")
FC.printCrimes(locale = 'annandale')
input('\n Press enter to filter by search key, this one being animal')
FC.printCrimes(searchKey = 'animal')
input('\n Press enter to filter by both search key (assault) and locale (fairfax)')
FC.printCrimes(searchKey = 'assault', locale = 'fairfax')
input("\n Press enter to filter by both search key (animal) and zip code (22030)")
FC.printCrimes(searchKey = 'animal', zip = '22030')
input('\n Press enter to test filtering by search key (larceny) and locale (mclean)')
FC.printCrimes(searchKey = 'larceny', locale = 'mclean')
input('\n Test 3. Press enter to test countByCrime function, starting with zip code 22150')
FC.countByCrime(select = '22150')
input('\n Press to test countByCrime for all zip codes')
FC.countByCrime()
input('\n Test 4. Press to run countByZip, displays crime percentages for all zip codes')
FC.countByZip()
input('\n Test 5. Press enter to create and print a list of crimes filtered by zip code, default zip code is 22030')
ZL = FC.zipCodeList()
print("\n\nList created for ZL\n")
for c in ZL:
    print(c)
input('\n Test of zipCodeList with a different zip code of 20191')
NZL = FC.zipCodeList(zip = '20191')
for c in NZL:
    print(c)

print("End of program")
