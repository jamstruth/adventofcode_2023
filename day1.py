import sys
import re

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
    
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    DIGIT_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ALL_DIGITS = DIGITS + DIGIT_WORDS
    
    DIGIT_WORDS_REGEX = '|'.join(DIGIT_WORDS)
    
    FULL_REGEX = fr'(\d|{DIGIT_WORDS_REGEX})'
    
    def calculate_line(self, line):
        # filter the line to only numbers
        print(line)
        first_digit = self.get_first_digit(line)
        last_digit = self.get_last_digit(line)
        print(first_digit + last_digit)
        return int(first_digit + last_digit)
    
    def get_first_digit(self, line):
        curr_first_index = sys.maxsize
        first_digit = ''
        for substring in self.ALL_DIGITS:
            try:
                index = line.index(substring)
                if index < curr_first_index:
                    first_digit = self.get_numeric_string(substring)
                    curr_first_index = index
            except ValueError:
                continue
        return first_digit
    
    def get_last_digit(self, line):
        curr_last_index = 0
        last_digit = ''
        for substring in self.ALL_DIGITS:
            try:
                index = line.rindex(substring)
                if index > curr_last_index:
                    last_digit = self.get_numeric_string(substring)
                    curr_last_index = index
            except ValueError:
                continue
        return last_digit
            
    
    def get_numeric_string(self, number_string):
        if number_string.isnumeric():
            return number_string
        return str(self.DIGIT_WORDS.index(number_string))
        
        
    
print(Calculator(file_path).calculate_file())