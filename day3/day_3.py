import re

with open("day3/table.txt", "rt", encoding="utf-8") as infile:
	instructions = infile.read()

# mul(xxx,xxx)
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", instructions)


sum = 0
for match in matches:
	str1,str2 = match.split(",")
	num1 = int(str1.removeprefix("mul("))
	num2 = int(str2.removesuffix(")"))
	sum += num1 * num2


# part2

# first mul(xxx,xxx), then stop at don't(), then stop at do()
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)")
matches2 = pattern.findall(instructions)
sum2 = 0
do = True
for match in matches2:
	if (match.startswith("don't")):
		do = False
	elif match.startswith("do"):
		do = True
	elif do:
		str1, str2 = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", match).groups()
		num1 = int(str1)
		num2 = int(str2)
		sum2 += num1 * num2


print(f'part1: {sum}')
print(f'part2: {sum2}')