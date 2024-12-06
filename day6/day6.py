import numpy as np


with open("day6/input.txt", "rt") as infile:
	map = [l.strip() for l in infile.readlines()]

start = None
for x, line in enumerate(map):
	for y, c in enumerate(line):
		if c == "^":
			start = (x, y)
			break
	if start:
		break
		
else:
	start = (0, 0)
	print("no start")

print(f"start: {start}")

def bounds(map, pos):
    x, y = pos
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def move(map, pos, dir, loop_i):
	x,y = pos
	dx, dy = dir
	next = (x + dx, y + dy)
	if bounds(map, next) and map[next[0]][next[1]] == "#":
		loop_i = (loop_i + 1) % len(dirs)
		return pos, dirs[loop_i], loop_i
	return next, dir, loop_i

    #  up       right   down    left
dirs = [(-1,0), (0,1), (1, 0), (0, -1)]
inside = True
in_loop = False
walked = set()
loop_detect = set()
pos = start
d = dirs[0]
loop_i = 0
while inside and not in_loop:
	walked.add(pos)
	loop_detect.add((pos, d))
	pos, d, loop_i = move(map, pos, d, loop_i)

	in_loop = (pos, d) in loop_detect
	inside = bounds(map, pos)

# print(walked)
print(f'part 1: {len(walked)}')


# for row in enumerate(map):
# 	for col in enumerate(line):
