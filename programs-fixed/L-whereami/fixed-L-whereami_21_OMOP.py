
from typing import List
from collections import defaultdict

def main():
    
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    
    dist = [[0]*201 for _ in range(201)]
    x, y, dx, dy = 100, 100, 0, 1
    t_p, t_g = 0, 1
    cur = 0

    while 0 <= y < 201 and 0 <= x < 201:
        dist[y][x] = cur
        x += dx
        y += dy
        t_p += 1
        if t_p == t_g:
            dx, dy = dy, -dx
            t_p = 0
            if dy:
                t_g += 1
        cur += 1

    obs = defaultdict(list)
    for i, (ty, tx, tv) in enumerate(g):
        for x in range(tx, tx + tv):
            for y in range(ty, ty + tv):
                if 0 <= y < 201 and 0 <= x < 201:
                    obs[dist[y][x]].append(i)

    cnt = [0] * N
    turned = [0] * N
    sizes = [len(obs[i]) for i in range(N)]

    t = 0
    while obs[t]:
        v = obs[t]
        v.sort(key=lambda x: cnt[x])
        v.reverse()
        i, j = 0, 0
        while i < len(v):
            j += 1
            while j < len(v) and cnt[v[j]] == cnt[v[i]]:
                j += 1
            size = sizes[cnt[v[i]]]
            if j - i != size:
                if j - i == 1:
                    turned.append(t)
                size -= j - i
                sizes[cnt[v[i]]] = size
                if size == 1:
                    turned[cnt[v[i]]] = t
                for k in range(i, j):
                    cnt[v[k]] = len(turned) - 1
                sizes.append(j - i)
            i = j
        t += 1

    print(f'{(sum(turned) / N + 1) * 2:.9f}')
    print(max(turned) * 2 + 1)
    print(' '.join(map(lambda x: str(x + 1), [i for i in range(N) if turned[i] == max(turned)])))

if __name__ == "__main__":
    main()
