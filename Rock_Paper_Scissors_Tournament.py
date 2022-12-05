import os.path
import sys
from Rock_Paper_Scissors.Rock import Rock
from Rock_Paper_Scissors.Paper import Paper
from Rock_Paper_Scissors.Scissors import Scissors
from Rock_Paper_Scissors.Shoot import Shoot

# Setup variables for future computation.
filepath = "Resources\\Rock_Paper_Scissors_Tournament.txt"
points_part_1 = 0
points_part_2 = 0

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

# Go line by line and resolve each round.
for line in lines:
    players = line.strip().split(' ')
    # Part 2, you react to the opponent based on whether you should win, lose or draw.
    points_part_2 += Shoot(players[0], players[1]).resolve_round()
    if players[1] == 'X':
        # Part 1, you play rock.
        points_part_1 += Rock(players[0]).resolve_round()
    if players[1] == 'Y':
        # part 1, you play paper.
        points_part_1 += Paper(players[0]).resolve_round()
    if players[1] == 'Z':
        # part 1, you play scissors.
        points_part_1 += Scissors(players[0]).resolve_round()

file.close()

# Print out solutions.
print(f'Total Score at end of tournament: {points_part_1} (Part 1)')
print(f'Total Score at end of tournament: {points_part_2} (Part 2)')
