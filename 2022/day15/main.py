with open('input.txt', 'r') as file: 
	sensors = [i.strip().replace('Sensor at ', '').replace(': closest beacon is at', ',').split(', ') for i in file.readlines()]
	sensors = [[int(i[2:]) for i in s] for s in sensors]
	beacons = [(bx, by) for _, _, bx, by in sensors]

	n = []
	ans = 0
	y = 10
	for sx, sy, bx, by in sensors: 	
		dist = abs(sx-bx) + abs(sy-by)

		for x in range(sx-dist, sx+dist+1): 
			if abs(sx-x) + abs(sy-y) <= dist and (x, y) not in beacons and (x, y) not in n: 
				n.append((x, y))
				ans += 1

	print(ans)


