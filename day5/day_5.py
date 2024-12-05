from functools import cmp_to_key 

key, update = open("day5/input.txt").read().split("\n\n")
pairs = []
for line in key.splitlines():
    left, right = line.split("|")
    pairs.append((int(left), int(right)))

manual = []
for line in update.splitlines():
    entries = [int(entry) for entry in line.split(",")]
    manual.append(entries)

# print(pairs)
# print(manual)

def comp(a, b):
    for left, right in pairs:
        if a == left and b == right:
            return 1
        if a == right and b == left:
            return (-1)
    return 0

p1 = 0
p2 = 0
for entry in manual:
    valid = all(
        (left not in entry) or (right not in entry) or (entry.index(left) < entry.index(right))
        for left, right in pairs
    )
    if (valid):
        p1 += entry[len(entry) // 2] #middle
    else:
        fix = sorted(entry, key=cmp_to_key(comp))
        p2 += fix[len(fix) // 2]


print (p1)
print (p2)