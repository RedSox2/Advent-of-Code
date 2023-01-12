with open('input.txt', 'r') as file: 
	f = file.read().strip()
	pairs = [i.strip() for i in f.split('\n\n')]
	lines = [i.strip() for i in f.split()]

pairs = [i.split('\n') for i in pairs]

def compare(left, right): 
	while len(left) > 0 and len(right) > 0:
		l, r = left.pop(0), right.pop(0)

		if type(l) == int and type(r) == int: 
			if l < r: 
				return 1
			elif l > r: 
				return 0

		elif type(l) == list and type(r) == int: 
			if (a := compare(l, [r])) != -1: 
				return a
		elif type(l) == int and type(r) == list: 
			if (a := compare([l], r)) != -1: 
				return a
		elif type(l) == list and type(r) == list: 
			if (a := compare(l, r)) != -1: 
				return a
	if len(left) < len(right): 
		return 1
	elif len(left) > len(right): 
		return 0
	else: 
		return -1


total = 0
for n, (a, b) in enumerate(pairs): 
	if compare(eval(a), eval(b)) == 1: 
		total += n + 1
print(total)

decoder1 = [[2]]
decoder2 = [[6]]

ind1, ind2 = 1, 2

while len(lines) > 0: 
	l = lines.pop(0)

	if len(l) == 0: 
		continue
	if compare(eval(l), [[2]]) == 1: 
		ind1 += 1
	if compare(eval(l), [[6]]) == 1: 
		ind2 += 1
print(ind1, ind2, ind1*ind2)
