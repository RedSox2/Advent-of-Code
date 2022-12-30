from sys import argv
with open(f'{argv[1]}.txt', 'r') as file: 
	file = file.read()
	groups1 = [i.replace('\n', '') for i in file.strip().split('\n\n')]
	groups2 = [i.split() for i in file.strip().split('\n\n')]
# part 1
total = sum(len(set(i)) for i in groups1)
print(total)

# part 2
total = 0
for g in groups2: 
	for i in set(max(g, key=lambda x: len(x))): 
		if all(i in n for n in g): 
			total += 1
print(total)


