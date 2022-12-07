with open("Inputs/7.txt") as f:
    history = f.readlines()[1:]

current_dir = "/"
# Dir: Size map
sizes = {"/":0}
for line in history:
    # Shell command
    if line.startswith("$"):
        if "$ cd" in line:
            folder = line[len("$ cd "):].strip()
            if folder == "..":
                current_dir = current_dir.rsplit("/", 2)[0] + "/"
                continue
            current_dir += f"{folder}/"
            sizes[current_dir] = 0
        else: # ls
            ''
    elif line.startswith("dir"):
        pass # We'll eventually cd automatically
    else: # File with size
        size = int(line.split(" ")[0])
        dir = current_dir
        while True:
            sizes[dir] += size
            if dir == "/":
                break
            dir = dir.rsplit("/", 2)[0] + "/"

print(sum([size for size in sizes.values() if size <= 100_000]))

# Part 2

TOTAL_SPACE = 70_000_000
NEED = 30_000_000

free_space = TOTAL_SPACE - sizes["/"]
to_be_deleted = NEED - free_space
print(min([size for size in sizes.values() if size >= to_be_deleted]))