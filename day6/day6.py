import numpy as np


with open("day6/input.txt", "rt") as infile:
	map = [list(l.strip()) for l in infile.readlines()]

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

marked_map = [row[:] for row in map]

for x, y in walked:
    marked_map[x][y] = 'x'

# Print the marked map
# for line in marked_map:
#     print("".join(line))

print(f'part 1: {len(walked)}')

def check_infinite_loop(map, start, new_obstacle_pos):
    map[new_obstacle_pos[0]][new_obstacle_pos[1]] = "#"
    pos = start
    d = dirs[0]
    loop_i = 0
    walked = set()
    loop_detect = set()
    inside = True
    in_loop = False

    while inside and not in_loop:
        walked.add(pos)
        loop_detect.add((pos, d))
        pos, d, loop_i = move(map, pos, d, loop_i)

        in_loop = (pos, d) in loop_detect
        inside = bounds(map, pos)

    map[new_obstacle_pos[0]][new_obstacle_pos[1]] = "."
    return in_loop

sum =0 
for new_obs_pos in walked:
	if (check_infinite_loop(map, start, new_obs_pos)):
		sum += 1

print(f"part 2: {sum}")