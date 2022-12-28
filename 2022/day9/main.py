<<<<<<< HEAD
<<<<<<< HEAD
def vect(a, b):
    return tuple(x + y for x, y in zip(a, b))


with open('input.txt', 'r') as file:
    cmds = file.read().strip()
    cmds = [i.strip().split() for i in cmds.split('\n')]
    # print(cmds)

    headc = (0, 0)
    tail = (0, 0)

    headl = (0, 0)

    visited = [(0, 0)]
    
    for dr, count in cmds:
            if dr == 'U':
                vector = (0, 1)
            elif dr == 'D':
                vector = (0, -1)
            elif dr == 'L':
                vector = (-1, 0)
            elif dr == 'R':
                vector = (1, 0)
            
            for i in range(int(count)):
                new = vect(headc, vector)
                if not -2 <= new[0]-tail[0] <= 2 or not -2 <= new[1]-tail[0] <= 2: 
                    tail = headl
                headl = headc
                headc = new
                if tail not in visited: 
                    visited.append(tail)
                if cmds.index([dr, count]) < 10: print(headc, headl, tail)
    print(len(visited))

=======
=======
>>>>>>> b36885e (add files from mac mini)
from sys import argv
neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)]
with open('input.txt') as file: 
	cmds = file.read().strip()
	cmds = [i.strip().split() for i in cmds.split('\n')]

	# print(cmds)

	directions = {
		"U": (0, 1),
		"D": (0, -1),
		"L": (-1, 0),
		"R": (1, 0)
	}

	rope = [(0, 0) for i in range(10)]

	last = [(0, 0) for i in range(10)]

	visited = [(0, 0)]
	v = [(0, 0)]

	print(f"BEGINNING OF INPUT #{argv[1]}")	
	

	for dr, count in cmds: 
		dx, dy = directions[dr]
		for i in range(int(count)): 
			last[0] = rope[0]

			rope[0] = (rope[0][0]+dx, rope[0][1]+dy)

			for i in range(1, len(rope)): 
				last[i] = rope[i]
				o = i-1
				ix, iy = rope[i]
				ox, oy = rope[o]
				if rope[i] not in neighbors(ox, oy): 
					if ix != ox and iy != oy: 
						cols = ox - ix
						rows = oy - iy
						if abs(cols) == abs(rows): 
							rope[i] = (rope[i][0]+cols//2, rope[i][1]+rows//2)
						elif abs(cols) > abs(rows): 
							rope[i] = (rope[i][0]+cols//2, oy)
						elif abs(rows) > abs(cols): 
							rope[i] = (ox, rope[i][1]+rows//2)
					else: 
						if ix == ox: 
							rope[i] = (ix, rope[i][1]+((oy-iy)//2))
						elif iy == oy: 
							rope[i] = (rope[i][0]+((ox-ix)//2), iy)

			if rope[9] not in visited: 
				visited.append(rope[9])
			print(dr, rope)

	print(len(visited))
<<<<<<< HEAD
>>>>>>> b36885e (add files from mac mini)
=======
>>>>>>> b36885e (add files from mac mini)

