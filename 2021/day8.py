from time import perf_counter
t = perf_counter()
from collections import Counter
from typing import Dict

with open("Inputs/8.txt") as f:
    raw_data = f.readlines()

def part1(d: str):
    data = map(lambda x: x.strip().split(' | ')[1], d)
    all_joined = " ".join(data)

    all_joined_lengths = map(lambda x: len(x), all_joined.split())
    print(Counter(all_joined_lengths))

#  1111
# 2    3
# 2    3
#  4444
# 5    6
# 5    6
#  7777

# fmt: off
digits = {
    "123567":  0,
    "36":      1,
    "13457":   2,
    "13467":   3,
    "2346":    4,
    "12467":   5,
    "124567":  6,
    "136":     7,
    "1234567": 8,
    "123467":  9,
}
# fmt: on

outputs = []
for line in raw_data:
    possible: Dict[int, str] = {}
    
    line = line.strip()
    output_words = line.split(' | ')[1].split()

    words = sorted(line.split(' | ')[0].split(), key=lambda x: len(x))
    one, seven, four, eigth = (x for x in words if len(x) not in {5,6})
    
    possible[1] = list(set(seven) - set(one))[0]

    zsn_letters = [letter for word in [x for x in words if len(x) == 6] for letter in word]
    zsn_missing_letters = [x for (x, y) in dict(Counter(zsn_letters)).items() if y == 2]
    
    possible[4] = list(set(four).intersection(set(zsn_missing_letters)).difference(set(one)))[0]

    possible[2] = list((set(four) - set(one)) - set(possible[4]))[0]

    five = [x for x in words if ((len(x) == 5) and (all(v[0] in x for v in possible.values() ) ))]
    assert five
    five = five[0]
    possible[6] = list(set(one).intersection(set(five).intersection(set(four))))[0]

    possible[3] = list(set(one) - set(five).intersection(set(four)))[0]

    nine = [x for x in words if ((len(x) == 6) and (set(four).issubset(set(x))))]
    assert nine
    nine = nine[0]
    possible[7] = list(set(nine) - (set(four).union(set(seven))))[0]
    possible[5] = list( set(eigth) - set(nine))[0]

    rev_possible = {v:k for k,v in possible.items()}
    number = ""

    for word in output_words:
        word_in_digit = "".join([str(rev_possible[c]) for c in word])
        number += str(digits["".join(sorted(word_in_digit))])
    
    outputs.append(int(number))

print(sum(outputs))
print(perf_counter()-t)