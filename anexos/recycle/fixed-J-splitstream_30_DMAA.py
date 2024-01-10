
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+1)]
mx = max(M, N)
for _ in range(1, N+1):
    ch, x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    if ch == 'S':
        nd[x].extend([0, y, z])
    else:
        nd[x].extend([y, z, 0])

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
    oin[nd[i][1]] = oin[nd[i][2]] = oout[nd[i][0]] = i

osz = [-1] * (mx+1)
osz[0] = M
def rec(x, sz):
    osz[x] = sz
    if oin[x] == 0:
        return
    v = nd[oin[x]]
    if osz[v[1]] == -1:
        return
    if v[0]:
        rec(v[2], osz[v[1]])
    else:
        rec(v[2], osz[v[1]]//2)
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
    while x != 1:
        v = nd[oout[x]]
        if v[0]:
            sz = min(osz[v[1]], osz[v[2]])
            if k <= 2 * sz:
                x = v[1 if k % 2 else 2]
                k = (k+1) // 2
            else:
                x = v[2 if osz[v[2]] > osz[v[1]] else 1]
                k -= sz
        else:
            k = 2 * k - (x == v[1])
            x = v[2]
    print(k)
