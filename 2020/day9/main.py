from itertools import accumulate
with open('input.txt', 'r') as file: 
	nums = [int(i) for i in file.read().strip().split('\n')]

	for n in range(26, len(nums)): 
		first = nums[n-25:n]
		t = nums[n]
		
		for i in first: 
			if t - i in first: 
				break
		else: 
			print(t)
			T = t
			break
	
	# part 2
	A = nums
	sums   = {s:i for i,s in enumerate(accumulate(A)) }
	result = [ [*range(i+1,sums[s+T]+1)] for s,i in sums.items() if s+T in sums ]
	result = [list(map(lambda x: nums[x], i)) for i in result]

	print(max(result[0]) + min(result[0]))
