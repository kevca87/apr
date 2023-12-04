import sys

# Establecer el nuevo límite de recursión
sys.setrecursionlimit(5000)

def doit(x, y):
    global g, X, Y, wm, wn
    ch = g[y][x] if 1 <= x <= X and 1 <= y <= Y else '.'
    if not ch:
        return
    for i in range(N):
        x2 = x + (wm[i] if ch == '.' else -wm[i])
        y2 = y + (wn[i] if ch == '.' else -wn[i])
        
        g[y2][x2] = ch
        doit(x2, y2)


while True:
    try:
        X, Y, N = map(int, input().split())
    except EOFError:
        break

    g = [['' for _ in range(X + 1)] for _ in range(Y + 1)]
    wm, wn = [0] * N, [0] * N

    for i in range(N):
        entrada = list(map(int, input().split()))
        wm[i], wn[i] = entrada[0], entrada[1]
        B = entrada[2]
        boundary_coordinates = entrada[3:]

        assert len(boundary_coordinates) == B * 2

        for j in range(0, len(boundary_coordinates), 2):
            x, y = boundary_coordinates[j], boundary_coordinates[j + 1]
            g[y][x] = '#'
            x2, y2 = x - wm[i], y - wn[i]
            if 1 <= x2 <= X and 1 <= y2 <= Y:
                g[y2][x2] = '.'

    for y in range(-Y, 2 * Y + 1):
        for x in range(-X, 2 * X + 1):
            doit(x, y)

    for y in range(1, Y + 1):
        print(''.join(g[y][x] if g[y][x] else '.' for x in range(1, X + 1)))
    print()

    for y in range(1, Y + 1):
        print(''.join(g[y][x] if g[y][x] else '#' for x in range(1, X + 1)))
    print()