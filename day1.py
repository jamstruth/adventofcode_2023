import sys
import re

file_path = sys.argv[1]

# Open file
f = open(file_path)

total = 0
for line in f.readlines():
    # filter the line to only numbers
    all_numbers = re.findall(r'\d', line)
    number = int(all_numbers[0] + all_numbers[-1])
    total = total + number
    
print(total)