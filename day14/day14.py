import keyboard
RED = "\033[91m"
RESET = "\033[0m"


with open("day14/input.txt") as infile:
	lines = infile.read().strip().split("\n")

cycles = 1
grid_size = 101,103
mid_grid = (grid_size[0] // 2, grid_size[1] // 2)
print(f"grid_size: {grid_size} middle: {mid_grid}")

def move(cycles):
		
	pos = []
	for i in range(len(lines)):
		line = lines[i]
		# p=x,y v=x,y
		p = line.split(" ")[0].split("=")[1]
		v = line.split(" ")[1].split("=")[1]
		px,py = p.split(",")
		vx,vy = v.split(",")
		final_px = (int(px)+int(vx) * cycles) % grid_size[0]
		final_py = (int(py)+int(vy) * cycles) % grid_size[1]
		# print(f"robot[{i}] pos:({final_px}, {final_py})")
		pos.append((final_px,final_py))
	return pos

def part_1(pos):
	q1 = 0
	q2 = 0
	q3 = 0
	q4 = 0
	for x, y in pos:
		if x < mid_grid[0] and y < mid_grid[1]:
			q1 += 1
		elif x > mid_grid[0] and y < mid_grid[1]:
			q2 += 1
		elif x < mid_grid[0] and y > mid_grid[1]:
			q3 += 1
		elif x > mid_grid[0] and y > mid_grid[1]:
			q4 += 1

	print()
	safety_score = q1 * q2 * q3 * q4

	print(f"\nq1 {q1} q2 {q2} q3 {q3} q4 {q4}")
	print(f"safety score = {safety_score}")


def print_grid(pos):
	pos_map = {}
	for x, y in pos:
		if (x,y) not in pos_map:
			pos_map[(x,y)] = 0
		pos_map[(x,y)] += 1

	for y in range(grid_size[1]):
		for x in range(grid_size[0]):
			count = pos_map.get((x,y), 0)
			if x == mid_grid[0] or y == mid_grid[1]:
				# print(" ", end="")
				print(f"{"*" if count > 0 else '.'}", end="")
				# print(f"{RED}{count if count > 0 else '.'}{RESET}", end="")
			else:
				# print(count if count > 0 else ".", end="")
				print("*" if count > 0 else ".", end="")
		print()

# part_1(move(100))


# don't do this......
i = 0
for i in range(10000):
	print(i)
	print_grid(move(i))
	print()
