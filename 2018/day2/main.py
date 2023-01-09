with open('input.txt', 'r') as file: 
	ids = [i.strip() for i in file.readlines()]

	twos = len([1 for i in ids if any(i.count(n) == 2 for n in i)])
	threes = len([1 for i in ids if any(i.count(n) == 3 for n in i)])

	print(twos*threes)

	for n in ids: 
		for i in ids: 
			if (a := [n[j] == i[j] for j in range(len(n))]).count(True) == len(n)-1:
				print(i, n)
				print(i[:a.index(False)] + i[a.index(False)+1:])
