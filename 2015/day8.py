# https://adventofcode.com/2015/day/8

# from re import sub

# with open("Inputs/day8.txt") as f:
#     strings = f.readlines()

# string_code_length = 0
# string_mem_length = 0

# pattern = r"\\x.."
# subst = "."
# # strings = ['"\""']
# for string in strings:
#     og_string = string
#     # Remove \n
#     string = string.strip()
#     to_be_added_code = len(string)
#     string_code_length += to_be_added_code
#     # Leave out the ""
#     string = string[1:-1]
#     subbed_string = sub(pattern, subst, string).replace('\\"','#').replace("\\\\","\\")
#     to_be_added_mem = len(subbed_string)
#     string_mem_length += to_be_added_mem

# print(string_code_length - string_mem_length)

import re

with open("Inputs/day8.txt") as f:
    input = f.readlines()

def part1():

    len_in_codes = []
    len_in_memory = []

    for line in input:
        line = line.strip()
        len_in_codes.append(len(line))
        line = line[1:-1]

        special = False
        parsed_line = ""
        hex_escape_count = 0
        hex_escape = ""
        for character in line:
            if special:
                match character:
                    case "\\":
                        special = False
                        parsed_line += "\\"
                    case '"':
                        special = False
                        parsed_line += '"'
                    case 'x':
                        hex_escape_count = 0
                        hex_escape = ""
                    case hex_char:
                        hex_escape_count += 1
                        hex_escape += hex_char
                        if (hex_escape_count == 2):
                            parsed_line += chr(int(hex_escape, 16))
                            special = False
                continue
                

            # Check if a special character is coming
            if character == "\\":
                special = True
                continue
            
            # Else append it to the str
            parsed_line += character               

        len_in_memory.append(len(parsed_line))
    return sum(len_in_codes) - sum(len_in_memory)

def part2():
    original_lengths = []
    new_lengths = []
    for line in input:
        line = line.strip()
        original_lengths.append(len(line))
        new_line = ""
        for character in line:
            special = character in ('"', '\\',)

            if special:
                match character:
                    case '\\':
                        new_line += "\\\\"
                    case '"':
                        new_line += '\\"'
                continue
            new_line += character
                        
        new_lengths.append(len(new_line) + 2)
    
    return sum(new_lengths) - sum(original_lengths)


print(part1())
print(part2())
