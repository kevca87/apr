
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+1)]
mx = 0
for _ in range(1, N+1):
  ch, x, y, z = input().split()
  x, y, z = map(int, (x, y, z))
  mx = max(mx, x, y, z)
  if ch == 'S':
      nd[x] = [0, y, z, 0]
  else:
      nd[x] = [y, z, 0, 0]

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
  oin[nd[i][1]] = oin[nd[i][2]] = oout[nd[i][0]] = i

osz = [-1] * (mx+1)
osz[0] = M
def rec(x, sz):
  osz[x] = sz
  v = nd[oin[x]]
  if v[0] == 0 or osz[v[1]] == 0 or osz[v[2]] == 0:
      return
  rec(v[1], (osz[v[0]]+1)//2)
  rec(v[2], osz[v[0]]//2)

rec(1, M)
for i in range(2, mx+1):
  if oout[i] == 0:
      rec(i, 0)

for _ in range(Q):
    x, k = map(int, input().split())
    if k > osz[x] or osz[x] == -1:
        print('none')
        continue
    while True:
        v = nd[x]
        if v[1] != 0:
            sz = osz[v[1]]
            if k <= sz:
                x = v[1]
            else:
                k -= sz
                x = v[2]
        else:
            print(v[2] + 1 if k == 1 else v[2])
            break
