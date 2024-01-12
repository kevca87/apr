
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+2)]
mx = 0
for _ in range(1, N+1):
  ch, x, y, z = input().split()
  x, y, z = int(x), int(y), int(z)
  mx = max(mx, x, y, z)
  if ch == 'S':
      nd[x] = [0, y, z]
  else:
      nd[x] = [y, z, 0]

oin = [0] * (mx+2)
oout = [0] * (mx+2)
for i in range(1, N+1):
  oin[nd[i][0]] = oin[nd[i][1]] = oout[nd[i][2]] =  i
  if len(nd[i]) > 3:
        oout[nd[i][3]] = i
osz = [-1] * (mx+2)
osz[0] = 0
def rec(x, sz):
  osz[x] = sz
  if oin[x] == 0:
      return
  v = nd[oin[x]]
  if osz[v[0]] == -1 or (len(v) > 2 and osz[v[1]] == -1):
      return
  if len(v) > 2:
      rec(v[2], osz[v[0]]+osz[v[1]])
  else:
      rec(v[1], (osz[v[0]]+1)//2)
      rec(v[2], osz[v[0]]//2)

rec(1, M)
for i in range(2, mx+2):
  if not oout[i]:
      rec(i, 0)

for _ in range(Q):
  x, k = map(int, input().split())
  if k > osz[x]:
      print("none")
      continue
  while x != 1:
      v = nd[oin[x]]
      if len(v) > 2:
          sz = min(osz[v[0]], osz[v[1]])
          if k <= 2 * sz:
              x = v[not k % 2]
              k = (k+1) // 2
          else:
              x = v[(osz[v[1]] > osz[v[0]]) + 1]
              k -= sz
      else:
          k = 2 * k - (v[1] == x)
          x = v[0]
  print(k)
