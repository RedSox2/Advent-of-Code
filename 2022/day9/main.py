def vect(a, b):
    return tuple(x + y for x, y in zip(a, b))


with open('input.txt', 'r') as file:
    cmds = file.read().strip()
    cmds = [i.strip().split() for i in cmds.split('\n')]
    # print(cmds)

    headc = (0, 0)
    tail = (0, 0)

    headl = (0, 0)

    visited = [(0, 0)]
    
    for dr, count in cmds:
            if dr == 'U':
                vector = (0, 1)
            elif dr == 'D':
                vector = (0, -1)
            elif dr == 'L':
                vector = (-1, 0)
            elif dr == 'R':
                vector = (1, 0)
            
            for i in range(int(count)):
                new = vect(headc, vector)
                if not -2 <= new[0]-tail[0] <= 2 or not -2 <= new[1]-tail[0] <= 2: 
                    tail = headl
                headl = headc
                headc = new
                if tail not in visited: 
                    visited.append(tail)
                if cmds.index([dr, count]) < 10: print(headc, headl, tail)
    print(len(visited))


