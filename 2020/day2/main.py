with open('input.txt', 'r') as file: 
	passwords = [i.strip().split() for i in file.readlines()]

# part 1
p1 = 0
for p in passwords: 
	start, end = [int(i) for i in p[0].split('-')]
	char = p[1][0]
	pas = p[2]
	if start <= pas.count(char) <= end: 
		p1 += 1
print(p1)

# part 2
p2 = 0
for p in passwords: 
	f, s = [int(i)-1 for i in p[0].split('-')]
	char = p[1][0]
	pas = p[2]
	if (pas[f] == char) ^ (pas[s] == char): 
		p2 += 1
print(p2)
