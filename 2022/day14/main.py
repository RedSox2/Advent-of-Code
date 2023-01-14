with open('input.txt', 'r') as file: 
	paths = [i.strip() for i in file.readlines()]
	paths = [[[int(num) for num in i.split(',')] for i in n.split(' -> ')] for n in paths]
	

occ = []

for n, path in enumerate(paths): 
	sx, sy = path[0]
	for ex, ey in path[1:]: 
		if sx == ex: 
			d = (ey - sy) // abs(ey - sy)
			Y = [i for i in range(sy, ey+d, d)]
			occ.extend(list(zip([sx]*len(Y), Y)))
		elif sy == ey: 
			d = (ex - sx) // abs(ex - sx)
			X = [i for i in range(sx, ex+d, d)]
			occ.extend(list(zip(X, [sy]*len(X))))
		sx, sy = ex, ey

occ = list(set(occ))

getrow = lambda n: [(x, y) for x, y in occ if y == n]
getcol = lambda n: [(x, y) for x, y in occ if x == n]

abyss = max(occ, key=lambda x: x[1])[1]

sand = 0

while True: 
	sx, sy = 500, 1
	rest = False
	while not rest and sy > abyss: 	
		if (sx, sy+1) in occ: 
			if (sx-1, sy+1) not in occ: 
				sx -= 1
				sy += 1
			elif (sx+1, sy+1) not in occ: 
				sx += 1
				sy += 1
			else: 
				rest = True
			
		

