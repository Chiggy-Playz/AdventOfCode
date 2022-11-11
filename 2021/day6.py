from pprint import pprint
with open("Inputs/6.txt") as f:
    lines = f.read()

fishes_input = list(map(lambda x: int(x),lines.split(',')))
n = 256

def old(n, fishes):

    for day in range(n):  # Run n times
        
        for f in range(0, len(fishes)):
            if fishes[f] > 0:
                fishes[f] -=1
            else: # 0 days since new
                fishes[f] = 6
                fishes.append(8)

    print(fishes)
    print(len(fishes))

# old(n, fishes_input.copy())

fishes = {x: 0 for x in range(9)}

for fi in fishes_input:
    fishes[fi] +=1 

for day in range(1, n+1):

    zero_fishes = fishes[0]

    for i in range(0, len(fishes)-1):
        fishes[i] = fishes[i+1]
    fishes[8] = 0
    fishes[6] += zero_fishes
    fishes[8] += zero_fishes
    # print(f"Day: {day}\nFishes: {fishes}\nTotal fishes: {sum(fishes.values())}\n")

print(sum(fishes.values()))