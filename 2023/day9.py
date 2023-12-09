from input_manager import get_input
import re

input = get_input(__file__)

numbers = [list(map(int, line.split(" "))) for line in input]

forward_prediction = 0
backward_prediction = 0

for history in numbers:

    sequences = [list(history)]
    sequence_no = 0
    while not all([x==0 for x in sequences[-1]]):
        new_sequence = []
        sequence = sequences[sequence_no]
        for i in range(len(sequence)-1):
            new_sequence.append(sequence[i+1] - sequence[i])
        sequences.append(new_sequence)
        sequence_no += 1
        
    for i, sequence in enumerate(sequences):
        forward_prediction += sequence[-1]
        backward_prediction += ((-1)**i) * sequence[0]

print(forward_prediction)
print(backward_prediction)