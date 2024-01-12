import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nd = [[] for _ in range(1)]
mx = 0
for _ in range(1, N+1):
  ch, x, y, z = input().split()
  x, y, z = int(x), int(y), int(z)
  mx = max(mx, x, y, z)
  nd.append([x] if ch == 'S' else [x, y, z])

oin = [0] * (mx+1)
oout = [0]* (mx+1)
for i in range(1, N+1):
  oin[nd[i][0]] = oin[nd[i][1]] = oout[nd[i][2]] = oout[nd[i][3]] = i if len(nd[i])==4 else i 

osz = [-1] * (mx+1)
osz[0] = 0
def rec(x, sz):
  osz[x] = sz
  if oin[x]==0: return
  v = nd[oin[x]]
  if osz[v[0]]==-1 or (osz[v[1]] == -1 and len(v)!=2): return
  rec(v[2] if len(v)==4 else v[1], (osz[v[0]]+osz[v[1]]) if len(v)==4 else (osz[v[0]]+1)//2)

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
      if len(v)==4:
          sz = max(osz[v[0]], osz[v[1]])
          if k <= sz:
              x = v[not k%2]
              k = (k+1) // 2
          else:
              x = v[0 if osz[v[0]] > osz[v[1]] else 2]
              k += sz
      else:
          x = v[0]
          k = 2 * k - 1
  print(k)