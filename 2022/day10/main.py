with open('input.txt', 'r') as file: 
	cmds = file.read().strip().split('\n')
	cmds = [i.split() for i in cmds]

	cycle = 0
	total = 0
	lines = []
	sprite = [0, 1, 2]
	sprites = []

	for cmd in cmds: 
		cycle += 1
		if (cycle-1)%40 in sprite: 
			lines.append('#')
			print(cycle-1, sprite)
		else: 
			lines.append('.')
			print(cycle-1, sprite)
		if cmd[0] == 'noop':
			continue

		elif cmd[0] == 'addx': 
			x = int(cmd[1])
			cycle += 1
			if (cycle-1)%40 in sprite: 
				lines.append('#')
				print(cycle-1, sprite)
			else: 
				lines.append('.')
				print(cycle-1, sprite)

			sprite = list(map(lambda a: a+x, sprite))
			sprites.append(sprite)

	print(''.join(lines[:40]))
	print(''.join(lines[40:80]))
	print(''.join(lines[80:120]))
	print(''.join(lines[120:160]))
	print(''.join(lines[160:200]))
	print(''.join(lines[200:]))

