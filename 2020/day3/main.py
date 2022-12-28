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
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for d, x in slopes: 
	c = 0 
	COLS = len(m[0])
	a = 0
	for i in m[::x]: 
		if i[c%COLS] == '#': 
			a += 1
		c += d
		if x == 2: print(c, m.index(i))
	p2 *= a
	print(a)
print(p2)
