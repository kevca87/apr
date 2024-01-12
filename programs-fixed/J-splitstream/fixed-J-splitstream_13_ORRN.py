
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
        nd[x] = [y, 0, z]
    else:
        nd[x] = [y, z]

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
    oin[nd[i][0]] = oin[nd[i][1]] = oout[nd[i][2]] = i

osz = [-1] * (mx+1)
osz[0] = 0

def rec(x, sz):
    osz[x] = sz
    if oin[x] == 0:
        return
    v = nd[oin[x]]
    if osz[v[0]] == -1:
        return
    if not v[1]:
        rec(v[2], (osz[v[0]]+1)//2)
        rec(v[2]+1, osz[v[0]]//2)
    elif v[1]:
        rec(v[2], osz[v[0]]+osz[v[1]])

rec(1, M)
for i in range(2, mx+1):
    if oin[i] == 0:
        rec(i, 0)

for _ in range(Q):
    x, k = map(int, input().split())
    if k > osz[x]:
        print("none")
        continue
    while x != 1:
        v = nd[oout[x]]
        if not v[1]:
            x = v[0]
        else:
            sz = min(osz[v[0]], osz[v[1]])
            if k > sz:
                x = v[1]
                k -= sz
            else:
                x = v[0]
    print(k)
