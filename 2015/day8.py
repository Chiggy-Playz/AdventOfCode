# https://adventofcode.com/2015/day/8

from re import sub

with open("Inputs/day8.txt") as f:
    strings = f.readlines()

string_code_length = 0
string_mem_length = 0

pattern = r"\\x.."
subst = "."
# strings = ['"\""']
for string in strings:
    og_string = string
    # Remove \n
    string = string.strip()
    to_be_added_code = len(string)
    string_code_length += to_be_added_code
    # Leave out the ""
    string = string[1:-1]
    subbed_string = sub(pattern, subst, string).replace('\\"','#').replace("\\\\","\\")
    to_be_added_mem = len(subbed_string)
    string_mem_length += to_be_added_mem

print(string_code_length - string_mem_length)