# Import required modules
from sense_hat import SenseHat
from pathlib import Path
import electronicDie
import time
import csv
import sys
import datetime

sense = SenseHat()

sense.show_message("Welcome. Shake PI to roll the dice. First to 30 wins. Good luck!")
sense.clear()


# WriteCSV class used to import the results
# Into a CSV file, so it can be read
# By the user.

class WriteCSV:
    def __init__(self, date, player, winner_score):
        # Declare Variables
        self._date = date
        self._player = player
        self._winner_score = winner_score

    # If it's the first time, create a file with the write option.
    def first_time(self):
        with open("winner.csv", "w", newline="") as csvfile:
            self.writer = csv.writer(csvfile)
            self.writer.writerow(["Date", "Winner", "Winner Score"])
            csvfile.close()

    # Write contents to the CSV file with the append option, to not overwrite.
    def write(self):
        with open("winner.csv", "a", newline="") as csvfile:
            self.writer = csv.writer(csvfile)
            self.writer.writerow([self._date, str(self._player), str(self._winner_score)])
            csvfile.close()


class Game:
    def player_roll(self, player, score):
        sense.show_message("Your turn,")
        sense.show_message(str(player))
        game_roll = False
        while not game_roll:
            x, y, z = sense.get_accelerometer_raw().values()

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 1.5 or y > 1.5 or z > 1.5:
                roll_score = electronicDie.roll()
                time.sleep(2)
                sense.clear()
                time.sleep(1)
                game_roll = True

        cumulative_score = score + roll_score
        sense.show_message("You rolled,")
        sense.show_message(str(roll_score))
        sense.show_message("Your total score,")
        sense.show_message(str(cumulative_score))
        return cumulative_score

    def play_game(self):
        self.date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        self.p1score = 0
        self.p2score = 0
        self.winner_score = 0
        self.player = ""
        player1 = "P1"
        player2 = "P2"

        # Writing the CSV variables for creating
        # And appending the report.
        self._date = self.date
        self._winner_score = self.winner_score
        self._player = self.player
        self.writeCSV = None
        my_file = Path("winner.csv")

        while self.p1score < 30 and self.p2score < 30:
            self.p1score = self.player_roll(player1, self.p1score)
            if self.p1score >= 30:
                sense.show_message("Player 1 wins!")
                self.player = player1
                self.winner_score = self.p1score
                sense.clear()

                # Write contents to winner.CSV
                self.writeCSV = WriteCSV(self.date, self.player, self.winner_score)
                if not my_file.is_file():
                    self.writeCSV.first_time()
                self.writeCSV.write()
                sys.exit()
            else:
                self.p2score = self.player_roll(player2, self.p2score)
                if self.p2score >= 30:
                    sense.show_message("Player 2 wins!")
                    self.player = player2
                    self.winner_score = self.p2score
                    sense.clear()

                    # Write contents to winner.csv
                    self.writeCSV = WriteCSV(self.date, self.player, self.winner_score)
                    if not my_file.is_file():
                        self.writeCSV.first_time()
                    self.writeCSV.write()
                    sys.exit()


# The main class is used to control the program,
# It will initialize necessary variables and
# will load in the correct order
class Main:
    def __init__(self):
        run_game = Game()
        run_game.play_game()


# Call the main class, for the program to be executed.
Main()
