def safe(arr):
	diff = arr[1] - arr[0]

	for idx in range(len(arr) - 1):
		next_diff = arr[idx + 1] - arr[idx]
		# if same value, 		diff > +-3,			changes from inc to dec
		if (next_diff == 0 or abs(next_diff) > 3 or (next_diff > 0) != (diff > 0)):
			return False
		diff = next_diff
	return True

safe_first = 0
safe_second = 0
with open("day2/day2_table.txt", "rt", encoding="utf-8") as infile:
	for line in infile:
		nums = list(map(int, line.split()))
		if safe(nums):
			safe_first += 1
		else:
			for i in range(len(nums)):
				# make a new list with one element removed
				new_nums = nums[:i] + nums[i + 1 :]
				# if this list works, +1 safe, go to next line
				if (safe(new_nums)):
					safe_second += 1
					break


print(f"part1: {safe_first}")
print(f"part2: {safe_first + safe_second}")
