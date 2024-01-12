
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
      nd[x] = [y, 0, z, -1]
  else:
      nd[x] = [y, z, -1, -1]

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
  oin[nd[i][0]] = i
  oin[nd[i][1]] = i
  if nd[i][2] != -1:
    oout[nd[i][2]] = i
  if nd[i][3] != -1:
    oout[nd[i][3]] = i

osz = [-1] * (mx+2)
osz[0] = 0
def rec(x, sz):
  osz[x] = sz
  if oin[x] == 0:
      return
  v = nd[oin[x]]
  if osz[v[0]] == -1 or osz[v[1]] == -1:
      return
  if v[2] == -1:
      rec(v[0], (sz+1)//2)
      rec(v[1], sz//2)
  else:
      rec(v[0], sz)
      rec(v[1], sz)

rec(1, M)
for i in range(2, mx+1):
  if oout[i] == 0:
      rec(i, 0)

for _ in range(Q):
  x, k = map(int, input().split())
  if k > osz[x]:
      print("none")
      continue
  while k != 1:
      v = nd[oout[x]]
      if v[2] == -1:  
          if k <= osz[v[0]]:
              x = v[0]
          else:
              k -= osz[v[0]]
              x = v[1]
      else:
          x = v[0]
  print(k)
