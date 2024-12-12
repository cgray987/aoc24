with open("day11/input.txt") as infile:
    line = infile.read()
    stones = [int(x) for x in line.split()]

def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    else:
        return [stone * 2024]

def solve(it):
    cur_step = {int(n): 1 for n in line.split()}

    for i in range(it):
        next_step = {}
        for num in cur_step:
            for new_stone in blink(num):
                next_step[new_stone] = next_step.get(new_stone, 0) + cur_step[num]
        cur_step = next_step

    return sum(cur_step.values())

print(f"part 1: {solve(25)}")
print(f"part 2: {solve(75)}")