with open('input.txt', 'r') as file: 
	nums = [i.strip() for i in file.readlines()]

digits = [[] for i in range(len(nums[0]))]

for i in nums: 
	for n in range(len(i)): 
		digits[n].append(i[n])

# part 1
gamma = ''.join([max(set(i), key=i.count) for i in digits])

epsilon = ''.join([min(set(i), key=i.count) for i in digits])


gamma, epsilon = int(gamma, 2), int(epsilon, 2)

print(gamma*epsilon)

# part 2
oxygen = carbon = nums
bi = ['1', '0']

for i in range(len(oxygen[0])): 
	col = [n[i] for n in oxygen]
	most = max(bi, key=col.count)
	oxygen = [o for o in oxygen if o[i] == most]

	if len(oxygen) == 1: 
		break

for i in range(len(carbon[0])): 
	col = [n[i] for n in carbon]
	c1, c0 = col.count('1'), col.count('0')
	if c1 == c0: 
		least = '0'
	else: 
		least = '0' if c1 > c0 else '1'
	carbon = [c for c in carbon if c[i] == least]
	if len(carbon) == 1: 
		break

oxygen, carbon = int(oxygen[0], 2), int(carbon[0], 2)

print(oxygen*carbon)

