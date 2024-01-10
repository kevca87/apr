import sys
sys.setrecursionlimit(100000)  # Establece un l�mite m�s alto

def doit(x, y):
    ch = g[y][x] if (1 <= x <= X and 1 <= y <= Y) else '.'
    if ch == ' ':
        return
    for i in range(N):
        x2 = x + (wx[i] if ch == '.' else -wx[i])
        y2 = y + (wy[i] if ch == '.' else -wy[i])

        if 1 <= x2 <= X and 1 <= y2 <= Y:
            if g[y2][x2] == ' ':
                g[y2][x2] = ch
                doit(x2, y2)

while True:
    try:
        X, Y, N = map(int, input().split())
        g = [[' ' for _ in range(X + 1)] for _ in range(Y + 1)]
        wx = [0] * N
        wy = [0] * N
        for i in range(N):
            line = input().split()
            wx[i] = int(line[0])
            wy[i] = int(line[1])
            B = int(line[2])
            pos = 3
            for j in range(B):
                x = int(line[pos])
                pos = pos + 1
                y = int(line[pos])
                pos = pos + 1
                g[y][x] = '#'
                x2 = x - wx[i]
                y2 = y - wy[i]
                if 1 <= x2 <= X and 1 <= y2 <= Y:
                    g[y2][x2] = '.'

        for y in range(-Y, 2 * Y + 1):
            for x in range(-X, 2 * X + 1):
                doit(x, y)

        for y in range(1, Y + 1):
            for x in range(1, X + 1):
                print(g[y][x] if (g[y][x] != ' ') else '.', end='')
            print()
        print()

        for y in range(1, Y + 1):
            for x in range(1, X + 1):
                print(g[y][x] if (g[y][x] != ' ') else '#', end='')
            print()
    except EOFError:
        break