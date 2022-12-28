from sys import argv
f = argv[1] + '.txt'
with open(f, 'r') as file: 
	nums = [i.strip() for i in file.readlines()]

def sur(r, c): 
	ROWS = len(nums)
	COLS = len(nums[0])

	dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

	re = []

	for dr, dc in dirs: 
		nr, nc = r+dr, r+dc
		if (0 <= nr < ROWS) and (0 <= nc < COLS): 
			re.append((nr, nc))
	return re

print(sur(1, 1))

risk = 0
for r, j in enumerate(nums): 
	for c, i in enumerate(j): 
		i = int(i)
		for nr, nc in sur(r, c): 
			if int(nums[nr][nc]) >= i: 
				break
		else: 
			risk += i + 1
print(risk)
