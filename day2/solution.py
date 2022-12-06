from pathlib import Path

p = Path(__file__).with_name('input.txt')
f = open(p, 'r')
lines = f.readlines()

score = 0
lscore = 0
for line in lines:
    left = line[0]
    right = line[-2]
    
    if right == 'X':
        score += 1
        if left == 'A':
            score += 3
            lscore += 3
        elif left == 'B':
            lscore += 1
        elif left == 'C':
            score += 6
            lscore += 2

    elif right == 'Y':
        score += 2
        lscore += 3
        if left == 'B':
            score += 3
            lscore += 2
        elif left == 'A':
            score += 6
            lscore += 1
        elif left == 'C':
            lscore += 3

    elif right == 'Z':
        score += 3
        lscore += 6
        if left == 'C':
            score += 3
            lscore += 1
        elif left == 'B':
            score += 6
            lscore += 3
        elif left == 'A':
            lscore += 2

print(f"P1 Final Score: {score}")
print(f"P2 Final Score: {lscore}")
