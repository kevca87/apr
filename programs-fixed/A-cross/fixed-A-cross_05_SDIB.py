
import sys

sys.setrecursionlimit(5000)

def extend(x, y, g, X, Y, wm, wn, N):
    ch = g[y][x] if 1 <= x <= X and 1 <= y <= Y else '.'
    if not ch:
        return
    for i in range(N):
        x2 = x + (wm[i] if ch == '.' else -wm[i])
        y2 = y + (wn[i] if ch == '.' else -wn[i])
        if 1 <= x2 <= X and 1 <= y2 <= Y and not g[y2][x2]:
            g[y2][x2] = ch
            extend(x2, y2, g, X, Y, wm, wn, N)

while True:
    try:
        X, Y, N = map(int, input().split())
    except EOFError:
        break

    g = [['' for _ in range(X + 2)] for _ in range(Y + 2)]
    wm, wn = [0] * N, [0] * N

    for i in range(N):
        entry = list(map(int, input().split()))
        wm[i], wn[i] = entry[0], entry[1]
        B = entry[2]
        boundaries = entry[3:]

        for j in range(0, len(boundaries), 2):
            x, y = boundaries[j], boundaries[j + 1]
            g[y][x] = '#'
            x2, y2 = x - wm[i], y - wn[i]
            if 1 <= x2 <= X and 1 <= y2 <= Y:
                g[y2][x2] = '.'

    for y in range(1, Y + 1):
        for x in range(1, X + 1):
            extend(x, y, g, X, Y, wm, wn, N)

    for y in range(1, Y + 1):
        print(''.join(g[y][x] if g[y][x] else '.' for x in range(1, X + 1)))
    print()

    for y in range(1, Y + 1):
        print(''.join(g[y][x] if g[y][x] else '#' for x in range(1, X + 1)))
    print()

