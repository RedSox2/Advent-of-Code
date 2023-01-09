with open('input.txt', 'r') as file: 
	start, end = [int(i) for i in file.read().strip().split('-')]

	# part 1
	total = 0
	for n in range(start, end+1): 	
		n = str(n)

		digits = [int(i) for i in n]

		if all(digits[i] >= digits[i-1] for i in range(1, len(digits))) and any(digits[i] >= digits[i-1] for i in range(1, len(digits))): 
			total += 1

	print(total)
