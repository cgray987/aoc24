pairs = []

# read file into list of pairs
with open("day1/day1_table.txt", "rt") as infile:
	for line in infile:
		pairs.append(list(map(int, line.split())))

# get left and right elements
left = [int(pair[0]) for pair in pairs]
right = [int(pair[1]) for pair in pairs]

left.sort()
right.sort()

# after sorting, dist between the two values
distance = [abs(left - right) for left, right in zip(left, right)]

# number of times left appears in right, multiplied by itself
similar = [first * right.count(first) for first in left]

print(f'part 1: {sum(distance)}')
print(f'part 2: {sum(similar)}')

