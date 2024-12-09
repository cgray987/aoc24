from collections import defaultdict
from itertools import permutations

ants = defaultdict(list)
with open("day8/input.txt", "rt") as infile:
	for y, line in enumerate(infile):
		for x, char in enumerate(line.strip()):
			if char != ".":
				ants[char].append((x, y))
		print(f"{y}\t{line}", end="")

limits = (x, y)

antis = set()
for dist in ants:
	# find all pairs of antenneas 
	for ant1, ant2 in permutations(ants[dist], 2): 
		# x and y differences
		dx = ant2[0] - ant1[0]
		dy = ant2[1] - ant1[1]
		pos = (ant1[0] - dx, ant1[1] - dy)
		# if in grid limits
		if ((0 <= pos[0] <= limits[0])
	  	and (0 <= pos[1] <= limits[1])):
			antis.add(pos)

# print('\n', antis)
print(f"\npart 1: {len(antis)}")

antis = set()
for dist in ants:
	# find all pairs of antenneas 
	for ant1, ant2 in permutations(ants[dist], 2): 
		# x and y differences
		dx = ant2[0] - ant1[0]
		dy = ant2[1] - ant1[1]
		pos = ant1
		while 1:
			pos = (pos[0] - dx, pos[1] - dy)
			if ((0 <= pos[0] <= limits[0])
	  		and (0 <= pos[1] <= limits[1])):
				antis.add(pos)
			else:
				break
		antis.add(ant1)
print(f"part 2: {len(antis)}")