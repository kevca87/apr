
from typing import List
from collections import defaultdict

def main():
    
    Y, X = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(Y)]
    
    dist = [[0] * 201 for _ in range(201)]
    x, y, dx, dy, step, stepn, cur = 100, 100, 0, 1, 0, 1, 0

    while y < 201:
        dist[y][x] = cur
        x += dx
        y += dy
        step += 1
        if step == stepn:
            dx, dy = dy, -dx
            step = 0
            if dy:
                stepn += 1
        cur += 1

    obs = defaultdict(list)

    for y in range(Y):
        for x in range(X):
            if g[y][x] != 0:
                obs[dist[100 + y][100 + x]].append(Y * y + x)

    comp = [0] * (X * Y)
    compt = [0] * (X * Y)
    compsz = [1] * (X * Y)

    for t in range(40000):
        if t in obs:
            v = obs[t]
            v.sort(key=lambda x: comp[x])
            v.reverse()
            for _ in range(len(v)):
                i, j = 0, 0
                while j < len(v) and comp[v[j]] == comp[v[i]]:
                    j += 1
                if j < len(v) - 1 or (j == len(v) - 1 and comp[v[j]] != v[j]):
                    compsz.append(j - i)
                    if j - i != 1:
                        compt.append(t)
                    for k in range(i, j):
                        comp[v[k]] = len(compsz) - 1
                    compsz[comp[v[i]]] -= j - i

    mx = max(compt)
    tot = sum(compt)

    print(f"{tot / X / Y:.9f}")
    print(mx)

    first = True
    for i in range(X * Y):
        if compt[comp[i]] == mx:
            if not first:
                print(' ', end='')
            first = False
            print(f"({i % X + 1},{i // X + 1})", end='')

    print()


if __name__ == "__main__":
    main()
