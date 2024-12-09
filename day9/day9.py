
with open("day9/input.txt", "rt") as infile:
	input = infile.read().strip()

# getting the disks/sizes
next_disk = 0
files = {}
id_or_space = True
disk = {}
next_file_id = 0
for i in input:
	length = int(i)
	if id_or_space:
		files[next_file_id] = (next_disk, length)
		for location in range(length):
			disk[next_disk + location] = next_file_id
		next_file_id += 1
	next_disk += length
	id_or_space = not id_or_space
		
# moving files
disk_copy = disk.copy()
left = 0
right = max(disk_copy.keys())
while left < right:
	if right in disk_copy:
		file_id = disk_copy[right]
		del disk_copy[right]
		while left in disk_copy:
			left += 1
		disk_copy[left] = file_id
	right -= 1

# print disks
# for i in range(max(disk_copy.keys()) + 1):
#     if i in disk_copy:
#         print(disk_copy[i], end="")
#     else:
#         print(".", end="")
# print()

ans = 0
for location, id,  in disk_copy.items():
	ans += location * id
print(f"part 1: {ans}")


# part 2, moving whole files
compact_files = list(range(next_file_id - 1, -1, -1))
for file_id in compact_files:
	insert_pos = 0
	# find free space big enough
	while insert_pos < files[file_id][0]:
		if all(insert_pos + i not in disk for i in range(files[file_id][1])):
			for i in range(files[file_id][1]):
				del disk[files[file_id][0] + i]
				disk[insert_pos + i] = file_id
			break
		else:
			insert_pos += 1

ans = 0
for location, id,  in disk.items():
	ans += location * id
print(f"part 2: {ans}")