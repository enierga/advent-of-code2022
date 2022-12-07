from pathlib import Path
from typing import List

p = Path(__file__).with_name('input.txt')
f = open(p, 'r')
lines = f.readlines()

def create_interval(s: str) -> List[int]:
    return list(map(int, s.split('-')))

def merge_interval(a: List[int], b: List[int]) -> bool:
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    elif a[0] <= b[0] and a[1] >= b[1]:
        return True
    return False

def shmerge_interval(a: List[int], b: List[int]) -> bool:
    if a[0] >= b[0] and a[0] <= b[1]:
        return True
    elif a[1] >= b[0] and a[1] <= b[1]:
        return True
    elif b[0] >= a[0] and b[0] <= a[1]:
        return True
    elif b[1] >= a[0] and b[1] <= a[1]:
        return True
    return False

full_overlaps = 0
partial_overlaps = 0
for line in lines:
    intervals = line.split(',')
    interval1 = create_interval(intervals[0])
    interval2 = create_interval(intervals[1])

    full_overlaps += 1 if merge_interval(interval1, interval2) else 0
    partial_overlaps += 1 if shmerge_interval(interval1, interval2) else 0

print(f"Overlapping Intervals: {full_overlaps}")
print(f"Partial Overlap: {partial_overlaps}")