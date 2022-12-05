import os.path
import sys

# Setup variables for future computation.
filepath = "Resources\\Sample_Input.txt"

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

# Test file input
for line in lines:
    print(line)

file.close()
