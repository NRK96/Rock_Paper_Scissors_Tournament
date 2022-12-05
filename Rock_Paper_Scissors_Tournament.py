import os.path
import sys
from Rock_Paper_Scissors.Rock import Rock
from Rock_Paper_Scissors.Paper import Paper
from Rock_Paper_Scissors.Scissors import Scissors

# Setup variables for future computation.
filepath = "Resources\\Rock_Paper_Scissors_Tournament.txt"
points_part_1 = 0

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

# Go line by line and resolve each round.
for line in lines:
    players = line.strip().split(' ')
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

# Print out solution.
print(f'Total Score at end of tournament: {points_part_1}')