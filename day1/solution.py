from pathlib import Path
import heapq

p = Path(__file__).with_name('input.txt')
f = open(p, 'r')
lines = f.readlines()

maxElf = 0
currElf = 0
elves = []

for line in lines:
    if line == '\n':
        maxElf = max(currElf, maxElf)
        heapq.heappush(elves, currElf)
        currElf = 0
    else:
        currElf += int(line)

print(f"Max Elf: {maxElf}")
print(f"Top 3: {heapq.nlargest(3, elves)}, Total: {sum(heapq.nlargest(3, elves))}")