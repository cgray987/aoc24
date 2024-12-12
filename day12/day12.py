with open("day12/input.txt", "rt") as infile:
	map = [[c for c in line.strip()] for line in infile]

w,h = len(map[0]), len(map)

def get_plant(map, x, y):
	if 0 <= x < w and 0 <= y < h:
		return map[y][x]
	else:
		return " "
	
def find_region(plant, map, x, y, visited):
	visited.add((y, x))
	perimeter = 0
	area = 1
	corners = 0
	up,down,left,right = neighbors(plant, map, x, y)
	up_left, up_right, down_left, down_right = neighbor_neighbors(plant, map, x, y)

	for neighbor in [up, down, left, right]:
		if neighbor != plant:
			perimeter += 1
			
	# outside corners
	if up != plant and right != plant:
		corners += 1
	if right != plant and down != plant:
		corners += 1
	if down != plant and left != plant:
		corners += 1
	if left != plant and up != plant:
		corners += 1

	# inside corners
	if up_left != plant and up == plant and left == plant:
		corners += 1
	if up_right != plant and up == plant and right == plant:
		corners += 1
	if down_right != plant and down == plant and right == plant:
		corners += 1
	if down_left != plant and down == plant and left == plant:
		corners += 1

	dirs = [(up, -1, 0), (down, 1, 0), (left, 0, -1), (right, 0, 1)]
	for val, dy, dx in dirs:
		new_y, new_x = y + dy, x + dx
		if val == plant and (new_y, new_x) not in visited:
			a, p, c = find_region(plant, map, new_x, new_y, visited)
			area += a
			perimeter += p
			corners += c

	return area, perimeter, corners


def neighbors(plant, map, x, y):
	up = get_plant(map, x, y - 1)
	down = get_plant(map, x, y + 1)
	left = get_plant(map, x - 1, y)
	right = get_plant(map, x + 1, y)
	return up, down, left, right

def neighbor_neighbors(plant, map, x, y):
	up_l = get_plant(map, x-1, y-1)
	up_r = get_plant(map, x+1, y-1)
	down_l = get_plant(map, x-1, y+1)
	down_r = get_plant(map, x+1, y+1)
	return up_l, up_r, down_l, down_r

visited = set()
regions = {}
cost = 0
cost2 = 0
for i in range(h):
	for j in range(w):
		if (i, j) not in visited:
			plant = map[i][j]
			region = set()
			a, p, c = find_region(plant, map, j, i, visited)
			if a > 0:
				visited.update(region)
				if plant not in regions:
					regions[plant] = []
				regions[plant].append((a, p, c))
				cost += a * p
				cost2 += a * c

for plant in regions.keys():
	print(f"\nplant {plant}:")
	for idx, (area, perimeter, corners) in enumerate(regions[plant], 1):
		print(f" region{idx}:\ta = {area}\tp = {perimeter}\tc = {corners}")

print(f"\npart 1 cost: {cost}")
print(f"\npart 2 cost: {cost2}")


