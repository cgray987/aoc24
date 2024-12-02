def safe(report):
	diff = report[1] - report[0]

	for idx in range(len(report) - 1):
		next_diff = report[idx + 1] - report[idx]
		if (next_diff == 0 or abs(next_diff) > 3 or (next_diff > 0) != (diff > 0)):
			return False
		diff = next_diff
	return True

safe_first = 0
safe_second = 0
with open("day2_table.txt", "rt", encoding="utf-8") as infile:
	for line in infile:
		nums = list(map(int, line.split()))
		if safe(nums):
			safe_first += 1
		else:
			for i in range(len(nums)):
				new_nums = nums[:i] + nums[i + 1 :] # make a new list with one element removed
				if (safe(new_nums)):
					safe_second += 1
					break


print(f"part1: {safe_first}")
print(f"part2: {safe_first + safe_second}")
