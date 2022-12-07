from pathlib import Path
import string

p = Path(__file__).with_name('input.txt')
f = open(p, 'r')
lines = f.readlines()

def find_common(c1: str, c2: str, c3: str) -> str:
    for c in c1:
        if (c in c2) and (c in c3):
            print(f"common: {c}")
            return c

def calculate_prio(c: str) -> int:
    prio = 1 # letters are 0 index
    if c.isupper():
        prio += 26
    p = prio + string.ascii_lowercase.index(c.lower())
    print(f"priority: {p}\n")
    return p

priority = 0
for i in range(len(lines))[1:len(lines)-1:3]:
    s1 = lines[i-1]
    s2 = lines[i]
    s3 = lines[i+1]
    print(f"s1: {s1}\ns2: {s2}\ns3: {s3}")
    priority += calculate_prio(find_common(s1, s2, s3))

print(f"Total Priority: {priority}")
