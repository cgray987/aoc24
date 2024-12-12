

with open("day10/input.txt", "rt") as infile:
	lines = [[int(c) for c in line.strip()] for line in infile]

w, h = (len(lines[0]), len(lines))

def trail(x, y, counter, done):
	# check if trail has been counted
	if (counter == 9 and (x, y) not in done):
		done.add((x,y))
		return 1
	else:
		score = 0
		dirs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
		for x1, y1 in dirs:
			if (0 <= x1 < w and 0 <= y1 < h #in bounds
	   		and lines[x1][y1] == counter + 1): #gradual increase
				score += trail(x1, y1, lines[x1][y1], done)
		return score
	
# part1
score = 0
sum = 0
for i, row in enumerate(lines):
	for j, start in enumerate(row):
		if start == 0:
			score = trail(i, j, 0, set())
			print(f"trail #{i}: {score}")
			sum += score
print(f"part 1: {sum}")
print()

def rating(x, y, counter):
	# now it doesn't matter if we've been before
	if (counter == 9):
		return 1
	else:
		score = 0
		dirs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
		for x1, y1 in dirs:
			if (0 <= x1 < w and 0 <= y1 < h #in bounds
	   		and lines[x1][y1] == counter + 1): #gradual increase
				score += rating(x1, y1, lines[x1][y1])
		return score
	
# part1
rate = 0
sum = 0
for i, row in enumerate(lines):
	for j, start in enumerate(row):
		if start == 0:
			rate = rating(i, j, 0)
			print(f"trail #{i}: {rate}")
			sum += rate
print(f"part 2: {sum}")