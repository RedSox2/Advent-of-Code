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

abyss = max(occ, key=lambda x: x[1])[1]+1 # remove +2 for part 1

sand = 0

while True: 
	sx, sy = 500, 0
	rest = False
	while not rest: 	
		if sy == abyss: 
			rest = True
		elif (sx, sy+1) in occ: 
			if (sx-1, sy+1) not in occ: 
				sx -= 1
				sy += 1
			elif (sx+1, sy+1) not in occ: 
				sx += 1
				sy += 1
			else: 
				if (sx, sy) == (500, 0): 
					sand += 1
					break
				rest = True
		else: 
			sy += 1
	else: 
		occ.append((sx, sy))
		sand += 1
		continue
	print(sand)
	break
		

