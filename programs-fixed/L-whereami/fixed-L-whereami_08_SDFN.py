
from typing import List
from collections import defaultdict

def main():
    X, Y = map(int, input().split())
    g = [input().strip() for _ in range(Y)]
    g.reverse()
    
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
            if g[y][x] == 'X':
                for sy in range(Y):
                    for sx in range(X):
                        obs[dist[y - sy + 100][x - sx + 100]].append((x + sx) + (y + sy) * X)


    size = X * Y
    comp,comp_t,comp_sz = list(range(size)),[0]*size,[1]*size
    
    t = 0
    while len(set(comp)) < size:
        if obs[t]:
            obs[t].sort(key=lambda x: comp[x])
            i,j = 0,0
            while i < len(obs[t]):
                while j < len(obs[t]) and comp[obs[t][j]] == comp[obs[t][i]]:
                    j += 1
                if j-i != comp_sz[comp[obs[t][i]]]:
                    if j-i > 1:
                        comp_t[comp[obs[t][i]]] = t
                    for k in range(i,j):
                        comp[obs[t][k]] = size
                    comp_sz.append(j-i)
                    comp_sz[comp[obs[t][i]]] -= j-i
                    size += 1
                i = j
        t += 1

    
    mx = max(comp_t)
    tot = sum(comp_t)

    print(f"{tot / size:.12f}")
    print(mx)

    result = []
    for i in range(X * Y):
        if comp_t[comp[i]] == mx:
            result.append((i//X+1,i%X+1))

    result.sort(key=lambda x: (x[0], x[1]))
    for item in result:
        print(f"{item[0]} {item[1]}")

if __name__ == "__main__":
    main()
