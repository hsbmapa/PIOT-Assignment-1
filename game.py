#Import required modules
import electronicDie
from sense_hat import SenseHat
import time
import csv

sense = SenseHat()

sense.show_message("Welcome. Shake pi. First to 30 wins. Good luck!")
sense.clear()

class rollDie:
    def __init__(self, roll):
        self.roll = electronicDie.roll

class WriteCSV():
    def __init__(self, filename, winscore):
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