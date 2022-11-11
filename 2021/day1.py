with open('Inputs/1.txt') as f:
    inputs = f.readlines()
    
n = 0

for i in range(1, len(inputs)):

    if int(inputs[i].strip()) > int(inputs[i-1].strip()):
        n+=1

print(n)

# 3 sum
three_measurements = []

for i in range(0, len(inputs)-2):
    three_measurements.append(int(inputs[i].strip()) + int(inputs[i+1].strip()) + int(inputs[i+2].strip()))

n_3 = 0
for i in range(1, len(three_measurements)):
    if three_measurements[i] > three_measurements[i-1]:
        n_3+=1

print("Three sum :", n_3)