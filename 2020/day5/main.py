from sys import argv
with open(f'{argv[1]}.txt', 'r') as file: 
	passes = file.read().strip().split()
	
# part 1
ids = []
for p in passes: 
	row = p[:7]
	col = p[7:]

	r = 0
	for n, i in enumerate(row[::-1]): 
		if i == 'B': 
			r += 2**n

	c = 0
	for n, i in enumerate(col[::-1]): 
		if i == 'R': 
			c += 2**n
	ids.append((r*8)+c)

# part 2
for n in range(min(ids), max(ids)+1): 
	if n not in ids: 
		print(n)
	
