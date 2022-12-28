from numpy import roll
with open('input.txt', 'r') as file: 
	fish = [int(i) for i in file.read().strip().split(',')]

counts = [fish.count(i) for i in range(9)]

print(counts)

for i in range(256): 
	counts = roll(counts, -1)
	counts[6] += counts[8]
print(sum(counts))
