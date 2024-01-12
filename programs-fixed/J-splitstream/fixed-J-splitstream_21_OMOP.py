
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+1)]
mx = 0
for _ in range(1, N+1):
    ch, x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    mx = max(mx, x, y, z)
    if ch == 'S':
        nd[x] = [y, 0, None, z]
    else:
        nd[x] = [y, z, None, None]

oin = [None] * (mx+1)
oout = [None] * (mx+1)
for i in range(1, N+1):
    oin[nd[i][0]] = oin[nd[i][1]] = oout[nd[i][0]] = oout[nd[i][3]] = i

osz = [-1] * (mx+1)
osz[0] = 0

def rec(x, sz):
    osz[x] = sz
    if oin[x] is None:
        return
    v = nd[oin[x]]
    if osz[v[0]] == -1 or osz[v[1]] == -1:
        return
    if v[2]:
        rec(v[2], osz[v[0]]+osz[v[1]])
    elif v[1]:
        rec(v[0], (osz[v[1]]+1)//2)
        rec(v[3], osz[v[1]]//2)

rec(1, M)
for i in range(2, mx+1):
    if not oout[i]:
        rec(i, 0)

for _ in range(Q):
    x, k = map(int, input().split())
    if k > osz[x]:
        print("none")
        continue
    while x != 0:
        v = nd[oout[x]]
        if v[2] and k <= osz[v[0]]:
            x = v[0]
            k = (k+1) // 2
        else:
            x = v[1]
    print(k)
