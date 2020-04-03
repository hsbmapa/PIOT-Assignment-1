#Import required modules
import electronicDie
from sense_hat import SenseHat
import time
import csv

sense = SenseHat()

sense.show_message("Welcome. Shake pi. First to 30 wins. Good luck!")
sense.clear()

# rollDie class used to call 
# The electronicDie file and the roll method.
class rollDie:
    def __init__(self, roll):
        # Declare Variables
        self.roll = electronicDie.roll
    
    def getRoll(self):
        return self.roll

class Players:
    def scores(self, score, winscore):
        self.score = score
        self.winscore = winscore

# WriteCSV class used to import the results
# Into a CSV file, so it can be read
# By the user.
class WriteCSV():
    def __init__(self, winscore):
        # Declare Variables
        self.winscore = winscore

    # If it's the first time, create a file with the write option.
    def firstTime(self):
        with open("winner.csv", "w", newline="") as csvfile:
            self.writer = csv.writer(csvfile)
            self.writer.writerow(["Winner Score"])
            csvfile.close()

    # Write contents to the CSV file with the append option, to not overwrite.
    def write(self):
        with open("winner.csv", "a", newline="") as csvfile:
            self.writer = csv.writer(csvfile)
            self.writer.writerow([str(self.winscore)])
            csvfile.close()

# The main class is used to control the program,
# It will initialize necessary variables and
# will load in the correct order
class main():
    def __init__(self):
        self.rollDie = rollDie
        self.roll = self.rollDie.getRoll

        # Write CSV variables
        self.__writeCSV = None
        self.__firstTime = True

        

        # Write contents to CSV
        self.__writeCSV = WriteCSV(self.winscore)
        if (self.__firstTime):
            self.__writeCSV.firstTime()
            self.__firstTime = False
        self.__writeCSV.write()

        
        
