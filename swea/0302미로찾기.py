dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
 
def find(x, y):
    path = []
    for d in dxy:
        if miro[x+d[0]][y+d[1]] == '0' or miro[x+d[0]][y+d[1]] == '2':
            path.append(d)
        elif miro[x+d[0]][y+d[1]] == '3':
            path.append((0,0))
            break
    return path
 

for t in range(1, int(input())+1):
    N = int(input())
    miro = [0]*(N+2)
    for i in range(N+2):
        if i == 0 or i == N+1:
            miro[i] = ['1']*(N+2)
        else: 
            miro[i] = ['1'] + list(input()) + ['1']

    for r in range(1, N+1):
        if '2' in miro[r]:
            start = r, miro[r].index('2')
        if '3' in miro[r]:
            end = r, miro[r].index('3')
    x, y= start[0], start[1]
    stack = []
    while True:
        path = find(x, y)
        if not path:
            if stack:
                miro[x][y] = '1'
                ret = stack.pop()
                x    = ret[0]
                y = ret[1]
            else:
                print("#%d 0" %t)
                break
        elif path[-1] == (0,0):
            print("#%d 1" %t)
            break
        elif len(path) >= 3 or (len(path) == 2 and (x, y) == start):
            for _ in range(len(path)+ ((x, y) == start) -2):
                stack.append((x, y))
            x += path[0][0]
            y += path[0][1]
        elif len(path) == 2 or len(path) == 1:
            miro[x][y] = '1'
            x += path[0][0]
            y += path[0][1]