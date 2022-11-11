import copy
from typing import List

with open("Inputs/3.txt", "r") as f:
    inputs = f.read().splitlines()

masks = {4: 0xF, 8: 0xFF, 16: 0xFFF}
# inputs = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
bitsize = len(inputs[0])
gamma_rate = "".join(
    "0"
    if (bits:="".join([input[x] for input in inputs])).count("0") > bits.count("1")
    else "1"
    for x in range(bitsize)
)
gamma_rate = int(gamma_rate, 2)
epsilon_rate = ~gamma_rate & masks[4 if bitsize <= 5 else 16]
print("Gamma Rate :", gamma_rate)
print("Epsilon Rate :",epsilon_rate)
print("Total Power Consumption :",gamma_rate*epsilon_rate)

# Part 2

def rating(data: List[str], mode: str):
    for bit_position in range(bitsize):
        
        if len(data) == 1:
            break

        all_bits_in_current_pos = "".join(x[bit_position] for x in data)
        zero_bits = all_bits_in_current_pos.count('0')
        one_bits = all_bits_in_current_pos.count('1')
        if mode == 'O':
            most_common_bit = "1" if zero_bits <= one_bits else "0" # For oxygen
        else:
            most_common_bit = "0" if zero_bits <= one_bits else "1" # For Co2

        data = list(filter(lambda x: x[bit_position] == most_common_bit, data))
        
    return data

o2_inputs = copy.deepcopy(inputs)
co2_inputs = copy.deepcopy(inputs)

o2_rating = rating(o2_inputs,  'O')[0]
co2_rating = rating(co2_inputs, 'C')[0]
print()
print(f"Oxygen Rating: {int(o2_rating, 2)} ({o2_rating})")
print(f"Carbon Dioxide Rating: {int(co2_rating, 2)} ({co2_rating})")
print(f"Life Support Rating: {int(o2_rating, 2) * int(co2_rating, 2)}")
