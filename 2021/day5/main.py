from collections import defaultdict
with open('input.txt', 'r') as file: 
	lines = [i.strip().split(' -> ') for i in file.readlines()]
	lines = [[list(map(int, n.split(','))) for n in i] for i in lines]

coords = defaultdict(int)

for i in lines: 
	s, e = i
	sx, sy = s
	ex, ey = e
	try: 
		if abs((sx-ex)//(sy-ey)) == 1: 
			xstep = 1 if sx < ex else -1
			ystep = 1 if sy < ey else -1
			x = [i for i in range(sx, ex+xstep, xstep)]
			y = [i for i in range(sy, ey+ystep, ystep)]
			line = list(zip(x, y))
			for i in line: 
				coords[i] += 1
			continue
	except ZeroDivisionError: 
		pass
	if sx == ex: 
		line = [(sx, i) for i in range(min(sy, ey), max(sy, ey)+1)]
		for i in line: 
			coords[i] += 1
	elif sy == ey: 
		line = [(i, sy) for i in range(min(sx, ex), max(sx, ex)+1)]
		for i in line: 
			coords[i] += 1

ans = 0
for i in coords.values(): 
	if i > 1: 
		ans += 1

print(ans)
