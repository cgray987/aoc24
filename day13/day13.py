
"""
where A_x, A_y is A button movement, 
B_x, B_y is B button movement

| A_x * A + B_x * B = Px
| A_y * A + B_y * B = Py

[A_x, B_x][A] = [Px]
[A_y, B_y][B] = [Py]

A = (Px * B_y - B_x * P_y) / (A_x * B_y - B_x * A_y)
B = (A_x * P_y - P_x * A_y) / (A_x * B_y - B_x * A_y)
	where (A_x * B_y - B_x * A_y) != 0

"""

with open("day13/input.txt", "rt") as infile:
	input = infile.read().split("\n\n")

def parse(buttons):
	output = {}

	A, B, P = buttons.splitlines()
	output['A'] = [int(num.split("+")[1]) for num in A.split(":")[1].split(",")]
	output['B'] = [int(num.split("+")[1]) for num in B.split(":")[1].split(",")]
	output['P'] = [int(num.split("=")[1]) for num in P.split(":")[1].split(",")]
	return output

map = [parse(buttons) for buttons in input]

def solve_eq(buttons):

	Ax,Ay = buttons['A']
	Bx,By = buttons['B']
	Px,Py = buttons['P']

	D = (Ax * By) - (Bx * Ay)
	if D == 0:
		return 0, 0
	
	Da = Px * By - Bx * Py
	Db = Ax * Py - Px * Ay

	A = Da // D
	B = Db // D
	if Ax * A + Bx * B == Px and Ay * A + By * B == Py:
		return A, B
	else:
		return 0, 0

total = 0
i = 0
for buttons in map:
	i += 1
	A, B = solve_eq(buttons)
	cost = 3 * A + B
	# print(f"scenario {i}:\tA={A}\tB={B}\tcost={cost}")
	total += cost
print(f"\npart 1: {total}")

def parse2(buttons):
	output = {}

	A, B, P = buttons.splitlines()
	output['A'] = [int(num.split("+")[1]) for num in A.split(":")[1].split(",")]
	output['B'] = [int(num.split("+")[1]) for num in B.split(":")[1].split(",")]
	output['P'] = [10000000000000 + int(num.split("=")[1]) for num in P.split(":")[1].split(",")]
	return output

map2 = [parse2(buttons) for buttons in input]

total = 0
i = 0
for buttons in map2:
	i += 1
	A, B = solve_eq(buttons)
	cost = 3 * A + B
	# print(f"scenario {i}:\tA={A}\tB={B}\tcost={cost}")
	total += cost
print(f"\npart 2: {total}")