from math import lcm
with open('input.txt', 'r') as file: 
	data = file.read().split('\n\n')
	data = [[n.strip() for n in i.split('\n')[1:]] for i in data]

	# print(data)

	class Monkey: 
		def __init__(self, start, oper, div, yes, no): 
			self.items = start
			self.oper = oper
			self.div = div
			self.yes = yes
			self.no = no 
			self.inspected = 0
		def evaluate(self): 
			items = [eval(str(old)+self.oper) for old in self.items]
			self.inspected += len(items)
			yes = [i for i in items if i%self.div == 0]
			no = [i for i in items if i%self.div != 0]
			self.items.clear()
			return (yes, no)
		def print(self): 
			print(self.items, self.oper, self.div, self.yes, self.no, sep=', ')
	monkeys = []
	for stuff in data: 
		starting = [int(i) for i in stuff[0][16:].split(',')]
		# print(starting)

		operation = stuff[1][21:]
		# print(operation)

		divby = int(stuff[2].split()[-1])
		# print(divby)

		y = int(stuff[3].split()[-1])
		n = int(stuff[4].split()[-1])
		# print(y, n)

		monkeys.append(Monkey(starting, operation, divby, y, n))
	mod = lcm(*[i.div for i in monkeys])
	
	for round in range(10000): 
		thrown = []
		for i in monkeys: 
			y, n = i.evaluate()
			yes, no = i.yes, i.no
			y = list(map(lambda x: x%mod, y))
			n = list(map(lambda x: x%mod, n))
			monkeys[yes].items.extend(y)
			monkeys[no].items.extend(n)
		print(f"End of round {round}")
		for i in monkeys: 
			print(i.inspected, len(i.items))
		print("\n")

	inspect = [i.inspected for i in monkeys]
	a = max(inspect)
	inspect.remove(a)
	b = max(inspect)
	print(a*b)

