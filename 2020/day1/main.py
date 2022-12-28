with open('input.txt') as file: 
	nums = [int(i) for i in file.read().strip().split('\n')]

# part 1
for i in nums: 
	if 2020 - i in nums: 
		print((2020-i)*i)
		break

# part 2
for i in nums: 
	t = 2020 - i
	for n in nums: 
		if t - n in nums: 
			print(i * n * (t - n))
				
