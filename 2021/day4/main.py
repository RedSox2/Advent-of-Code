with open('input.txt', 'r') as file :
	bingo = file.read().strip().split('\n\n')
nums = [int(i) for i in bingo[0].split(',')]

# print(nums)

boards = [[[int(n) for n in i.split()] for i in board.split('\n')] for board in bingo[1:]]

selected = [[[False for n in i.split()] for i in board.split('\n')] for board in bingo[1:]]

def findrow(arr, x) -> int | None: 
	for n, i in enuemrate(arr): 
		if  x in i: 
			return n
	return None

def findcol(arr, x) -> int | None:
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


