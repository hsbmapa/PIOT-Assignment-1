# Import required modules
from sense_hat import SenseHat
import electronicDie
import time
import csv
import sys

sense = SenseHat()

# sense.show_message("Welcome. Shake pi. First to 30 wins. Good luck!")
sense.clear()


# rollDie class used to call
# The electronicDie file and the roll method.

class rollDie:
    def __init__(self, roll):
        # Declare Variables
        self.roll = electronicDie.roll()

    def getRoll(self):
        return self.roll


class game:
    def playerRoll(self, player, score):
        sense.show_message("Your turn,")
        sense.show_message(str(player))
        gameRoll = False
        while not gameRoll:
            x, y, z = sense.get_accelerometer_raw().values()

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 1.5 or y > 1.5 or z > 1.5:
                rollScore = electronicDie.roll()
                time.sleep(2)
                sense.clear()
                time.sleep(1)
                gameRoll = True

        cumulativeScore = score + rollScore
        sense.show_message("You rolled,")
        sense.show_message(str(rollScore))
        sense.show_message("Your total score,")
        sense.show_message(str(cumulativeScore))
        return cumulativeScore

    def playGame(self):
        p1score = 0
        p2score = 0
        player1 = "P1"
        player2 = "P2"

        while p1score < 30 and p2score < 30:
            p1score = self.playerRoll(player1, p1score)
            if p1score >= 30:
                sense.show_message("Player 1 wins!")
                sense.clear()
                sys.exit()
            else:
                p2score = self.playerRoll(player2, p2score)
                if p2score >= 30:
                    sense.show_message("Player 2 wins!")
                    sense.clear()
                    sys.exit()


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
        run_game = game()
        run_game.playGame()
        # self.rollDie = rollDie
        # self.roll = self.rollDie.getRoll

        # Write CSV variables
        self.__writeCSV = None
        self.__firstTime = True

        # Write contents to CSV
        self.__writeCSV = WriteCSV(self.winscore)
        if (self.__firstTime):
            self.__writeCSV.firstTime()
            self.__firstTime = False
        self.__writeCSV.write()


main()
