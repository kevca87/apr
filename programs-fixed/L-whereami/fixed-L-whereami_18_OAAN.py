Python
from typing import List
from collections import defaultdict

def main():
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0]*201 for _ in range(201)]
    x, y, dx, dy, step, stepn, cur = 100, 100, 0, 1, 0, 1, 0

    while y<201:
        dist[y][x] = cur
        x += dx
        y += dy
        step += 1
        if step == stepn:
            dx,dy = dy,-dx
            step = 0
            if dy: stepn += 1
        cur += 1

    obs = defaultdict(list)

    for y in range(N):
        for x in range(N):
            if g[y][x] > 0:
                for i in range(g[y][x]):
                    obs[dist[100+i][100+x]].append(y*N+x)
                    
    comp = [0]*N*N
    compt = [0]*N*N
    compsz = [1]*N*N
    t = 0

    while len(obs[t]) > 0:
        v = obs[t]
        v.sort(key=lambda x:comp[x])
        v.reverse()
        i,j = 0,0
        while i<len(v):
            j = i+1
            while j<len(v) and comp[v[j]] == comp[v[i]]:
                j += 1
            sz = compt[comp[v[i]]]
            if j-i != sz:
                if j-i == 1:
                    compt[len(compsz)] = t
                sz -= j-i
                compt[comp[v[i]]] = sz
                if sz == 1:
                    compt[comp[v[i]]] = t
                for k in range(i, j):
                    comp[v[k]] = len(compsz)
                compsz.append(j-i)
            i = j
        t += 1

    tot = sum(compt)
    mx = max(compt)

    print("%.9f" % (tot/N/N))
    print(mx)
    first = True
    for i in range(N*N):
        if compt[i] == mx:
            if not first:
                print(' ', end='')
            first = False
            print("(%d,%d)" % (i%N+1, i//N+1), end='')
    print()


if __name__ == "__main__":
    main()
