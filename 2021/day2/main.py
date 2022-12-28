with open('input.txt', 'r') as file: 
	cmds = [i.strip().split() for i in file.readlines()]

DIRS = {
	'up': -1,
	'down': 1
}

x = 0
y = 0
aim = 0

for cmd in cmds: 
	if cmd[0] != 'forward': 
		d = DIRS[cmd[0]]

		count = int(cmd[1])
		aim += d*count
	else: 
		count = int(cmd[1])
		x += count
		y += aim*count

print(x*y)
