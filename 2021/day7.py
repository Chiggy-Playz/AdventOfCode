from pprint import pprint

with open("Inputs/7.txt") as f:
    positions = list(map(lambda x: int(x), f.read().split(',')))

fuel_costs = {}

for p in positions:
    if p in fuel_costs:
        continue
    
    fuel_cost = 0
    for crab in positions:
        # For part one
        # fuel_cost += abs(crab - p) 
        dist = abs(crab - p)
        fuel_cost += sum(range(1, dist+1))
    
    fuel_costs[p] = fuel_cost

# pprint(fuel_costs)
min_cost = min(fuel_costs.values())
min_pos = list(fuel_costs.keys())[list(fuel_costs.values()).index(min_cost)]
print(f"Fuel cost for position {min_pos} is {min_cost}")
