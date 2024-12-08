from itertools import product

def checkops(left, right):
	ops = ['+', '*', '|']
	for ops in product(ops, repeat=len(right) - 1):
		if (eval(right, ops) == left):
			print(right, ops)
			return True
	return False
		
def eval(nums, ops):
	res = nums[0]
	i = 1
	while i < len(nums):
		if ops[i - 1] == '+':
			res += nums[i]
		elif ops[i - 1] == '*':
			res *= nums[i]
		elif ops[i - 1] == '|':
			res = int(str(res) + str(nums[i]))
		i += 1
	return res

sum = 0
with open("day7/input.txt", "rt") as infile:
	for full_line in infile:
		line = full_line.split(":")
		if len(line) == 2:
			left = int(line[0].strip())
			right = [int(x.strip()) for x in line[1].split()]
			if (checkops(left, right)):
				sum += left

print(f"part 1: {sum}")

