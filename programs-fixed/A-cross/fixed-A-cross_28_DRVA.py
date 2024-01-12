
import sys
sys.setrecursionlimit(10000) 

def doit(x, y):
    ch = g[y][x] if (1 <= x <= X and 1 <= y <= Y) else '.'
    if ch == ' ':
        return
    for i in range(N):
        x2 = x + (wm[i] if ch == '.' else -wm[i])
        y2 = y + (wn[i] if ch == '.' else -wn[i])
        
        if 1 <= x2 <= X and 1 <= y2 <= Y:
            if g[y2][x2] == ' ':
                g[y2][x2] = ch
                doit(x2, y2)


while True:
    try:
        X, Y, N = map(int, input().split())
        g = [[' ' for _ in range(X + 1)] for _ in range(Y + 1)]
        wm = [0] * N
        wn = [0] * N
        for i in range(N):
            wm[i], wn[i] = map(int, input().split())
            B = int(input())
            for j in range(B):  
                x, y = map(int, input().split())
                g[y][x] = '#'
                x2 = x - wm[i]
                y2 = y - wn[i]
                if 1 <= x2 <= X and 1 <= y2 <= Y:
                    g[y2][x2] = '.'

        for y in range(-Y, 2 * Y + 1):
            for x in range(-X, 2 * X + 1):
                doit(x, y)

        for y in range(1, Y + 1):
            for x in range(1, X + 1):
                print(g[y][x] if (g[y][x] != ' ') else '.', end='')
            print()
            
        for y in range(1, Y + 1):
            for x in range(1, X + 1):
                print(g[y][x] if (g[y][x] != ' ') else '#', end='')
            print()

    except EOFError:
        break
