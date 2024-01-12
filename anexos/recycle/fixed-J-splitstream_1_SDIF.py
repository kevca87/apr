
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(N+1)]
mx = max(M, N, Q)
for _ in range(1, N+1):
  ch, x, y, z = input().split()
  x, y, z = int(x), int(y), int(z)
  if ch == 'S':
      nd[x] = [y, z, 0, 0]
  else:
      nd[x] = [y, z, 0, 1]

oin = [0] * (mx+1)
oout = [0] * (mx+1)
for i in range(1, N+1):
  oin[nd[i][0]] = oin[nd[i][1]] = oout[nd[i][2]] = oout[nd[i][3]] = i

osz = [-1] * (mx+1)
osz[0] = 0
def rec(x, sz):
  if x == 0:
    return
  osz[x] = sz
  v = nd[oin[x]]
  if osz[v[0]] == -1 or osz[v[1]] == -1:
      return
  if v[3]:
      rec(v[2], osz[v[0]]+osz[v[1]])
  else:
      rec(v[0], (osz[v[2]]+1)//2)
      rec(v[1], osz[v[2]]//2)

rec(1, M)
for i in range(2, N+1):
    if osz[i]<0:
        rec(i, 0)

for _ in range(Q):
  x, k = map(int, input().split())
  if k > osz[x]:
      print("none")
  else:
      while x != 1:
          v = nd[oout[x]]
          if v[3]:
              sz = min(osz[v[0]], osz[v[1]])
              if k<=2*sz:
                  k = sz
                  x = v[int(k % 2 == 0)]
              else:
                  x = v[1+int(osz[v[0]] < osz[v[1]])]
                  k = k-sz
          else:
              x = v[int(k % 2 == 0)]
              k = (k+1)//2
      print(k)
