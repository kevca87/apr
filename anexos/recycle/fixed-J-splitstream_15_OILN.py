
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+1)]
mx = M
for _ in range(1, N+1):
    ch, x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    mx = max(mx, x, y, z)
    if ch == 'S':
        nd.append([x, 0, y, z])
    else:
        nd.append([x, y, z, 0])

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
    oin[nd[i][0]] = oin[nd[i][1]] = oout[nd[i][2]] = oout[nd[i][3]] = i

osz = [-1] * (mx+1)
osz[1] = M
def rec(x):
    if osz[x] >= 0:
        return osz[x]
    v = nd[oin[x]]
    if v[1]:
        osz[x] = rec(v[2]) + rec(v[3])
    else:
        osz[x] = (rec(v[2]) + 1) // 2
    return osz[x]

rec(mx)
for _ in range(Q):
    x, k = map(int, input().split())
    if k > osz[x]:
        print("none")
    else:
        while k > 1:
            v = nd[oin[x]]
            if v[1] and k <= osz[v[2]]:
                x = v[2]
            else:
                if v[1]:
                    k -= osz[v[2]]
                x = v[2 + (v[1] != 0)]
        print(x)
