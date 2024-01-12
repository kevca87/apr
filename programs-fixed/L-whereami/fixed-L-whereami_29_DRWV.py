
from typing import List
from collections import defaultdict

def main():
    
    Y, X = map(int, input().strip().split())
    g = [input().strip() for _ in range(Y)]

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
            if g[y][x] == '0':
                i = 0
                for sy in range(Y):
                    for sx in range(X):
                        obs[dist[100 + sy - y][100 + sx - x]].append(i)
                        i += 1

    compsz = [X * Y]
    comp = list(range(X * Y))
    compt = [0] * (X * Y)
    
    t = 0
    while len(compsz) <= X * Y:
        if t in obs:
            v = obs[t]
            v.sort(key=lambda x: comp[x], reverse=True)
            i, j = 0, 0
            while i < len(v):
                j += 1
                while j < len(v) and comp[v[j]] == comp[v[i]]:
                    j += 1
                sz = compsz[comp[v[i]]]
                if j - i != sz: 
                    if j - i == 1:
                        compt[comp[v[i]]] = t
                    sz -= j - i
                    compsz[comp[v[i]]] = sz
                    if sz == 1:
                        compt[comp[v[i]]] = t
                    for k in range(i, j):
                        comp[v[k]] = len(compsz)
                    compsz.append(j - i)
                i = j
        t += 1

    mx = max(compt)
    tot = sum(compt)

    print(f"{tot / (X * Y):.9f}")
    print(mx)

    first = True
    for i in range(X * Y):
        if compt[comp[i]] == mx:
            if not first:
                print(" ", end='')
            first = False
            print(f"({i % X + 1},{i // X + 1})", end='')
    print()

if __name__ == "__main__":
    main()
