import re

infile = open("day1_table.txt", "rt")
contents = infile.read()

pairs = re.findall(r'(\d+)\s+(\d+)', contents)

first_set = [int(pair[0]) for pair in pairs]
second_set = [int(pair[1]) for pair in pairs]

first_set.sort()
second_set.sort()

distance = [abs(first - second) for first, second in zip(first_set, second_set)]

similar = [first * second_set.count(first) for first in first_set]



for i in range(len(first_set)):
	print(first_set[i], ",", end="")
	print(second_set[i], " = ",end="")
	print(distance[i], " sim: ", end="")
	print(similar[i])

# print(distance)

print(sum(distance))
print(sum(similar))

