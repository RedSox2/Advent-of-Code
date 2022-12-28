with open('input.txt', 'r') as file: 
	depths = [int(i.strip()) for i in file.readlines()]

total = 0
for i in range(4, len(depths)+1): 
	if sum(depths[i-3:i]) > sum(depths[i-4:i-1]): 
		total += 1

print(total)

