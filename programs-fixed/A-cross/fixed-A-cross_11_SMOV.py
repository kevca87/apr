
import sys
sys.setrecursionlimit(5000)

def doit(x, y, ch):
    if x<1 or y<1 or x>X or y>Y or (g[y][x] and g[y][x] != ch):
        return
    g[y][x] = ch
    for i in range(N):
        x2 = x + ((-wm[i]) if ch == '.' else wm[i])
        y2 = y + ((-wn[i]) if ch == '.' else wn[i])
        doit(x2, y2,ch)

while True:
    try:
        X, Y, N = map(int, input().split())
    except EOFError:
        break
    g = [['' for _ in range(X + 2)] for _ in range(Y + 2)]
    wm, wn = [0]*N, [0]*N
    for i in range(N):
        entrada= list(map(int,input().split()))
        wm[i],wn[i],B = entrada[0], entrada[1], entrada[2]
        for i in range(B):
            x, y = entrada[3+i*2], entrada[3+i*2+1]
            g[y][x]= '#'
            x2,y2 = x + wm[i], y+wn[i]
            if 1 <= x2 <= X and 1 <= y2 <= Y and g[y2][x2] != '#':
                g[y2][x2]= '.'
    for y in range(1, Y+2):
        for x in range(1, X+2):
            if not g[y][x]:
                doit(x,y,'.')
            if g[y][x] != '#':
                doit(x,y,'.')
    for i in range(1, Y + 1):
        print(''.join(g[i][j] if g[i][j] else '#' for j in range(1, X + 2)))
    print()
    for i in range(1, Y + 1):
        print(''.join(g[i][j] if g[i][j] else '.' for j in range(1, X + 2)))
    print()
