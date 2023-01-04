with open('input.txt', 'r') as file: 	
	nums = [int(i.strip()) for i in file.readlines()]

	ans = 0
	for i in nums: 
		# part 1
		# ans += i//3-2

		# part 2
		n = i
		while True: 	
			if (a := n//3-2) > 0: 
				ans += a
				n = a
			else: 
				break
			
	print(ans)
