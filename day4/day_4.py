with open("day4/input.txt", "rt", encoding="utf-8") as infile:
    instructions = infile.read()

# Convert the input string to a 2D array (table)
arr = [list(line) for line in instructions.splitlines()]

s = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for y in range(len(arr)):
    for x in range(len(arr)):
        for dy, dx in dirs:
            if 0 <= y + 3*dy < len(arr) and 0 <= x + 3*dx < len(arr):
                if arr[y][x] == 'X' and arr[y + dy][x + dx] == 'M' and arr[y + 2 * dy][x + 2 * dx] == 'A' and arr[y + 3 * dy][x + 3 * dx] == 'S':
                    s += 1
print(f'XMAS found {s} times')

# part 2
s = 0

# M.S
# .A.
# M.S
for y in range(len(arr)):
    for x in range(len(arr)):
        # MAS
        if arr[y][x] == 'M': 
            if y + 2 < len(arr) and x + 2 < len(arr[0]):
                if arr[y+1][x+1] == 'A' and arr[y+2][x+2] == 'S':
                    if (arr[y+2][x] == 'M' and arr[y][x+2] == 'S') or (arr[y+2][x] == 'S' and arr[y][x+2] == 'M'):
                        s += 1
        # SAM
        if arr[y][x] == 'S':
            if y + 2 < len(arr) and x + 2 < len(arr[0]):
                if arr[y+1][x+1] == 'A' and arr[y+2][x+2] == 'M':
                    if (arr[y+2][x] == 'M' and arr[y][x+2] == 'S') or (arr[y+2][x] == 'S' and arr[y][x+2] == 'M'):
                        s += 1
print(f'XMAS found {s} times')
