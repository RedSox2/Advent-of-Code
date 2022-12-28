with open('input.txt', 'r') as file :
	bingo = file.read().strip().split('\n\n')
nums = [int(i) for i in bingo[0].split(',')]

# print(nums)

boards = [[[int(n) for n in i.split()] for i in board.split('\n')] for board in bingo[1:]]

selected = [[[False for n in i.split()] for i in board.split('\n')] for board in bingo[1:]]

<<<<<<< HEAD
def findrow(arr, x) -> int | None: 
	for n, i in enuemrate(arr): 
		if  x in i: 
=======
def findrow(arr, x) -> int | None:
	for n, i in enumerate(arr):
		if  x in i:
>>>>>>> b36885e (add files from mac mini)
			return n
	return None

def findcol(arr, x) -> int | None:
<<<<<<< HEAD
	for i in arr: 
		if x in i: 
			return i.index(x)
	return None

def check(board: list[bool], nr: int, nc: int) -> bool: 
		diag1 = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
		diag2 = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
		
		row = board[nr]
		col = [i[nc] for i in board]
		
		if all(row) == 1: 
			return True
		if all(col) == 1: 
			return True
		if (nr, nc) in diag1: 
			if all(board[dr, dc] for dr, dc in diag1): 
				return True
		if (nr, nc) in diag2: 
			if all(board[dr, dc] for dr, dc in diag2): 
				return True
		return False


for num in nums: 
	num = int(num)
	for ind, board in enumerate(boards): 
		if (fr := findrow(board, num)

=======
	for i in arr:
		if x in i:
			return i.index(x)
	return None

def check(board: list[bool], nr: int, nc: int) -> bool:
		row = board[nr]
		col = [i[nc] for i in board]

		if all(row) == 1:
			return True
		if all(col) == 1:
			return True
		return False

scores = []
print(len(boards))
for num in nums:
	num = int(num)
	rm = []
	srm = []
	for ind, board in enumerate(boards):
		if (fr := findrow(board, num)) is not None: 
			fc = findcol(board, num)
			selected[ind][fr][fc] = True

			if check(selected[ind], fr, fc): 
				total = 0
				for r, n in enumerate(board): 
					for c, i in enumerate(n): 
						total += i if not selected[ind][r][c] else 0
				scores.append(total*num)
				rm.append(board)
				srm.append(selected[ind])
	for i in rm: boards.remove(i)
	for i in srm: selected.remove(i)
print(scores)
print(len(scores), len(boards))
>>>>>>> b36885e (add files from mac mini)

