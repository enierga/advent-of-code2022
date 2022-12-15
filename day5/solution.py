from pathlib import Path
from typing import List

p = Path(__file__).with_name('input.txt')
f = open(p, 'r')
lines = f.readlines()

stacks = {x: [] for x in range(len(lines[0])//4)}

def move_crates(crates: int, fr: int, to: int):
    for i in range(crates):
        crate = stacks[fr-1].pop(-1)
        stacks[to-1].append(crate)
    print(stacks)

for line in lines:
    if line == '\n' or line == ' ': continue
    elif line[0] != 'm':
        for i in range(len(line)):
            if line[i] == '[':
                stacks[i//4].insert(0, line[i+1])
    else:
        inputs = line.replace('\n', '').split(' ')
        for x in ['move', 'from', 'to']: inputs.remove(x)
        move_crates(int(inputs[0]), int(inputs[1]), int(inputs[2]))

final_crate = []
for key in range(8):
    final_crate.append(stacks[key][-1])
print(f"Top of crate stacks: {final_crate}")
