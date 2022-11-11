# https://adventofcode.com/2015/day/4

from hashlib import md5

secret_key = "ckczppom"
decimal = 0
# part 1: 5, part 2: 6
length = 5 

while True:
    string = f"{secret_key}{decimal}"
    hash = md5(string.encode("utf-8")).hexdigest()
    if hash.startswith("0" * length):
        break
    decimal += 1

print(decimal)