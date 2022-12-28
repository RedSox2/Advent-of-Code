from string import ascii_lowercase
from collections import deque
with open('input.txt', 'r') as file: 
	data = file.read().strip()
	G = [i.strip() for i in data.split('\n')]

	startr = [n for n, i in enumerate(G) if 'S' in i][0]
	startc = [n for n, i in enumerate(G[startr]) if 'S' == i][0]
	G[startr] = list(G[startr])
	G[startr][startc] = 'a'
	G[startr] = ''.join(G[startr])
	endr = [n for n, i in enumerate(G) if 'E' in i][0]
	endc = [n for n, i in enumerate(G[endr]) if 'E' == i][0]
	G[endr] = list(G[endr])
	G[endr][endc] = 'z'
	G[endr] = ''.join(G[startr])

	ROWS = len(G)
	COLS = max(len(i) for i in G)
	
	def sur(r, c): 
		x = []
		dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

		for dr, dc in dirs: 
			if -1 < r+dr < ROWS and -1 < c+dc < COLS: 
				x.append((r+dr, c+dc))
		return x


	alphabet = ascii_lowercase
	alphadict = {}
	for n, i in enumerate(alphabet): 
		alphadict[i] = alphabet[:n+2]
	def lee(r, c, tr, tc):
		visited = [[False for i in range(COLS)] for i in range(ROWS)]
		queue = deque()

		try: 
			if (G[r][c] != 'a' or G[tr][tc] != 'z'):
				return -1
		except IndexError: 
			return -1

		start = (r, c, 0)
		queue.append(start)
		visited[r][c] = True


		while queue: 
			qr, qc, dist = queue.popleft()

			if (qr, qc) == (tr, tc): 
				return dist
			for ar, ac in sur(qr, qc): 
				if G[ar][ac] in alphadict[G[qr][qc]] and not visited[ar][ac]: 
					queue.append((ar, ac, dist+1)) 
					visited[ar][ac] = True
		return -1
                    
	# PART 1
	print(lee(startr, startc, endr, endc))                

	# PART 2
	a = []
	for r, row in enumerate(G): 
		for c, i in enumerate(row): 
			if i == 'a':
				a.append(lee(r, c, endr, endc))
	a = [i for i in a if i > 0]
	print(min(a))
				
