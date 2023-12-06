import sys
import re

from numpy import number

file_path = sys.argv[1]



class Calculator:
    
    def __init__(self, file_path):
        self.file_path = file_path
        
    def calculate_file(self):
        # Open file
        with open(file_path) as f:
            total = 0
            for line in f.readlines():
                total = total + self.calculate_line(line)
        return total
    
    DIGIT_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    DIGIT_WORDS_REGEX = '|'.join(DIGIT_WORDS)
    
    FULL_REGEX = fr'({DIGIT_WORDS_REGEX})|\d'
    
    def calculate_line(self, line):
        # filter the line to only numbers
        all_digits = re.findall(self.FULL_REGEX, line)
        print(self.FULL_REGEX)
        print(all_digits)
        first_digit = self.get_numeric_string(all_digits[0])
        last_digit = self.get_numeric_string(all_digits[-1])
        return int(first_digit + last_digit)
    
    def get_numeric_string(self, number_string):
        if number_string.isnumeric():
            return number_string 
        return self.DIGIT_WORDS.index(number_string)
        
        
    
print(Calculator(file_path).calculate_file())