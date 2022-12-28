from sys import argv

f = argv[1]

with open(f+'.txt', 'r') as file: 
	codes = [i.strip() for i in file.readlines()]
	codes = [i.split('|')[1].strip().split() for i in codes]

total = 0
for i in codes: 
	for n in i: 
		if len(n) in [2, 4, 3, 7]: 
			total += 1

print(total)

