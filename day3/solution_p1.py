from pathlib import Path
import string

p = Path(__file__).with_name('input.txt')
f = open(p, 'r')
lines = f.readlines()

def find_common(c1: str, c2: str) -> str:
    for c in c1:
        if c in c2:
            return c

def calculate_prio(c: str) -> int:
    prio = 1 # letters are 0 index
    if c.isupper():
        prio += 26
    return prio + string.ascii_lowercase.index(c.lower())

priority = 0
for line in lines:
    s1 = line[:len(line)//2]
    s2 = line[len(line)//2:]
    
    priority += calculate_prio(find_common(s1, s2))

print(f"Total Priority: {priority}")
