
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(M+1)]
mx = max(M, N)
for _ in range(N):
    ch, x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    if ch == 'S':
        nd[y] = [x, 0, z, z+1]
    else:
        nd[x] = [0, y, z, z+y+1]

oin = [(0, 0)] * (mx+1)
oout = [(0, 0)] * (mx+1)
for i in range(1, N+1):
    oin[nd[i][2]] = oin[nd[i][3]] = oout[nd[i][0]] = oout[nd[i][1]] = i

osz = [0] * (mx+1)
def rec(x, sz):
    osz[x] = sz
    if oin[x][0] == 0:
        return
    v = nd[oin[x][0]]
    if osz[v[0]] == -1 or osz[v[1]] == -1:
        return
    if v[1]:
        rec(v[2], osz[v[0]]+osz[v[1]])
    else:
        rec(v[1], (osz[v[0]]+1)//2)
        rec(v[3], osz[v[0]]//2)
rec(1, M)
for i in range(2, mx+1):
    if not oout[i][0]:
        rec(i, 0)

for _ in range(Q):
    x, k = map(int, input().split())
    if k > osz[x]:
        print("none")
    else:
        print(k if k != 0 else "none")
