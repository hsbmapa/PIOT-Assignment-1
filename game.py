#Import required modules
import electronicDie
from sense_hat import SenseHat
import time
import csv

sense = SenseHat()

class WriteCSV():
    def __init__(self, filename, winscore):
        # Declare Variables
        self.__winscore = winscore

    # If it's the first time, create a file with the write option.
    def firstTime(self):
        with open("winner.csv", "w", newline="") as csvfile:
            self.__writer = csv.writer(csvfile)
            self.__writer.writerow(["Winner Score"])
            csvfile.close()

    # Write contents to the CSV file with the append option, to not overwrite.
    def write(self):
        with open("winner.csv", "a", newline="") as csvfile:
            self.__writer = csv.writer(csvfile)
            self.__writer.writerow([str(self.__winscore)])
            csvfile.close()