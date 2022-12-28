with open('input.txt', 'r') as file: 
	pairs = file.read().strip().split('\n\n')

pairs = [i.split('\n') for i in pairs]

def flatten(S):
	if S == []:
		return S
	if isinstance(S[0], list):
		return flatten(S[0]) + flatten(S[1:])
	return S[:1] + flatten(S[1:])

total = 0
print(len(pairs))
for n, parts in enumerate(pairs): 
	left, right = parts
	left, right = flatten(eval(left)), flatten(eval(right))

	for i in range(len(right)): 
		try: 
			if left[i] < right[i]: 
				total += n+1
				break
		except IndexError: 
			total += n+1
			break
print(total)
