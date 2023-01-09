with open('input.txt', 'r') as file: 
	lines = file.read().strip().split('\n')

	l1 = [i for i in lines[0].split(',')]
	l2 = [i for i in lines[1].split(',')]

	x1, y1 = 0, 0
	x2, y2 = 0, 0

	line1 = []
	line2 = []

	for d in l1: 
		if d[0] == 'U': 
			line1.extend([(x1, i) for i in range(y1+1, y1+int(d[1:])+1)])
			y1 += int(d[1:])
			
		elif d[0] == 'D': 
			line1.extend([(x1, i) for i in range(y1-1, y1-int(d[1:])-1, -1)])
			y1 -= int(d[1:])

		elif d[0] == 'L':
			line1.extend([(i, y1) for i in range(x1-1, x1-int(d[1:])-1, -1)])
			x1 -= int(d[1:])

		elif d[0] == 'R': 
			line1.extend([(i, y1) for i in range(x1+1, x1+int(d[1:])+1)])
			x1 += int(d[1:])


	intersections = []
	for d in l2: 
		if d[0] == 'U': 
			intersections.extend([(x2, i) for i in range(y2+1, y2+int(d[1:])+1) if (x2, i) in line1])
			y2 += int(d[1:])
			
		elif d[0] == 'D': 
			intersections.extend([(x2, i) for i in range(y2-1, y2-int(d[1:])-1, -1) if (x2, i) in line1])
			y2 -= int(d[1:])

		elif d[0] == 'L':
			intersections.extend([(i, y2) for i in range(x2-1, x2-int(d[1:])-1, -1) if (i, y2) in line1])
			x2 -= int(d[1:])

		elif d[0] == 'R': 
			intersections.extend([(i, y2) for i in range(x2+1, x2+int(d[1:])+1) if (i, y2) in line1])
			x2 += int(d[1:])

	print(len(set(line1)))
	distances = [abs(x) + abs(y) for x, y in intersections]
	print(min(distances))
