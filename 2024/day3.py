from common.input_manager import get_input
import re

input = get_input(__file__, lines=False)

pattern = r"mul\((\d+),(\d+)\)"

p1 = 0

for (a,b) in re.findall(pattern, input):
    p1 +=int(a) * int(b)

print(p1)

enabled = True
p2 = 0
do_dont_pattern = r"(don\'t\(\))|(do\(\))"
ops = list(re.finditer(pattern, input))
do_dont = list(re.finditer(do_dont_pattern, input))
i = 0 
j = 0

for op in ops:
    start = op.span()[0]
    # Check what occurs before this, do or dont
    for modifier in do_dont:
        if not modifier.span()[0] < start:
            break
        if "don" in modifier.group():
            enabled = False
        else:
            enabled = True 
    
    if enabled:
        a, b = map(int, op.groups())
        p2 += a * b

print(p2)