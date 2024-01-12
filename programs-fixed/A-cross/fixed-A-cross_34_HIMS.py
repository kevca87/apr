
import sys
sys.setrecursionlimit(10000)

def doit(x, y):
    if not(1 <= x <= X and 1 <= y <= Y):
        return
    ch = g[y][x]
    if ch == ' ':
        return
    for i in range(N):
        x2 = x + (wm[i] if ch == '.' else -wm[i])
        y2 = y + (wn[i] if ch == '.' else -wn[i])
        if not(1 <= x2 <= X and 1 <= y2 <= Y):
            continue
        if g[y2][x2] == ' ':
            g[y2][x2] = ch
            doit(x2, y2)

while True:
    try:
        X, Y, N = map(int, input().strip().split())
        g = [[' ' for _ in range(X + 2)] for _ in range(Y + 2)]
        wm = [0] * N
        wn = [0] * N
        for i in range(N):
            line = list(map(int, input().strip().split()))
            wm[i] = line[0]
            wn[i] = line[1]
            B = line[2]
            for j in range(B):
                g[line[2*j+4]][line[2*j+3]] = '#'
                x2 = line[2*j+3] - wm[i]
                y2 = line[2*j+4] - wn[i]
                if 1 <= x2 <= X and 1 <= y2 <= Y:
                    g[y2][x2] = '.'
        for y in range(1, Y + 1):
            for x in range(1, X + 1):
                doit(x, y)
        for y in range(1, Y + 1):
            print(''.join(g[y][1:X+1]))
        print()
        for y in range(1, Y + 1):
            for x in range(1, X + 1):
                g[y][x] = '#' if g[y][x] == ' ' else g[y][x]
            print(''.join(g[y][1:X+1]))
    except EOFError:
        break
