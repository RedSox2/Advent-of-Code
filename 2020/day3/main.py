with open('input.txt', 'r') as file: 
	m = [i.strip() for i in file.readlines()]

# part 1
c = 3
COLS = len(m[0])
p1 = 0
for i in m[1:]: 
	if i[c%COLS] == '#': 
		p1 += 1
	c += 3
print(p1)

# part 2
p2 = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1)]
for d, _ in slopes: 
	c = d 
	COLS = len(m[0])
	a = 0
	for i in m[1:]: 
		if i[c%COLS] == '#': 
			a += 1
		c += d	
	p2 *= a
for i in range(1, len(i), 2): 
	
