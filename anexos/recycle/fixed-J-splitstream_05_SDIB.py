

import sys

sys.setrecursionlimit(100000)
M, N, Q = map(int, input().split())

mf = [0]*(M+2)

def f(u, d):
    if mf[u] != -1:
        return
    mf[u] = d
    f(ee[u][0], d+1)
    if ed[u]:
        f(ed[u], d-1)

N += 1
en, ee, ed, ds = [0]*N, [[0, 0] for _ in range(N)], [0]*N, [0]*(M+1)
mf = mf+[-1]*N
for i in range(2, N+1):
    op, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    en[a], en[b], en[c] = i, i, i
    ee[i] = [a, b]
    if op == 'M':
        ed[i] = c
        e, f = sorted([a, b], key = lambda x: ds[x])
        ds[c] = ds[e]+1
        ds[b] = ds[f]+1
    else:
        ed[i] = b
        ds[b] = ds[a]+1
mf[M+1] = M
f(en[M+1], M)
for i in range(Q):
    a, b = map(int, input().split())
    if mf[a] > b:
        a = ee[en[a]][mf[ee[en[a]][0]] <= b]
        print(a)
    else:
        print(-1)
