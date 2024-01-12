
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+1)]
mx = 0
for _ in range(1, N+1):
  ch, x, y, z = input().split()
  x, y, z = map(int, [x, y, z])
  mx = max(mx, x, y, z)
  x += 1
  if ch == 'S':
      nd[x] = [0, y, z, 0]
  else:
      nd[x] = [y, z, 0, 0]

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
  oin[nd[i][0]], oin[nd[i][1]], oout[nd[i][2]], oout[nd[i][3]] = i, i, i, i

osz = [-1] * (mx+2)
osz[0] = 0
def rec(x, sz):
  osz[x] = sz
  if oin[x] == 0:
      return
  v = nd[oin[x]]
  if (osz[v[0]] == -1) or (osz[v[1]] == -1):
      return
  if v[1]:
      rec(v[2], osz[v[0]]+osz[v[1]])
  else:
      rec(v[2], (osz[v[0]]+1)//2)
      rec(v[3], osz[v[0]]//2)

rec(1, M)
for i in range(2, mx+1):
  if not oout[i]:
      rec(i, 0)

for _ in range(Q):
  x, k = map(int, input().split())
  if k > osz[x+1]:
      print("none")
      continue
  while x != 1:
      v = nd[oout[x]]
      if v[1]:
          sz = min(osz[v[0]+1], osz[v[1]+1])
          if k <= 2 * sz:
              x = v[(k % 2) == 1]
              k = (k+1) // 2
          else:
              x = v[osz[v[1]+1] > osz[v[0]+1]]
              k -= 2 * sz
      else:
          k = 2 * k if v[2] != x else 2 * k - 1
          x = v[0]
  print(k)
