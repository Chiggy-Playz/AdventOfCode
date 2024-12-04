from common.input_manager import get_input

input = get_input(__file__)

l1, l2 = [], []

for line in input:
    num1, num2 = line.split()
    l1.append(int(num1))
    l2.append(int(num2))

l1.sort()
l2.sort()

part1 = 0

for i, j in zip(l1, l2):
    part1 += abs(i-j)

print(part1)

part2 = 0
for i in l1:
    part2 += l2.count(i) * i

print(part2)
