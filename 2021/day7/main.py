from sys import argv

f = argv[1]

with open(f+'.txt', 'r') as file: 
	nums = [int(i) for i in file.read().strip().split(',')]

fuels = []
for i in range(min(nums), max(nums)+1): 
	dist = []
	for n in nums: 
		dist.append(sum(i for i in range(1, abs(n-i)+1)))
	print(i, dist)
	fuels.append(sum(dist))
	

print(min(fuels))
