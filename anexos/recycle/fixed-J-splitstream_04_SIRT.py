
import sys
sys.setrecursionlimit(100000)

M,N,Q = map(int,input().split())
nd = [[] for _ in range(N)]
mx = max(M,N,Q)
oin = [0]*(mx+2)
ot = [0]*(mx+2)
oout = [0]*(mx+2)
sz = [0]*(mx+2)

def rec(x):
    if ot[x]: 
        return sz[x]
    ot[x] = 1
    v = nd[oin[x]]
    sz[x] = rec(v[2]) if v[1] else rec(v[2]) + rec(v[3])
    return sz[x]

for i in range(1,N+1):
  v = input().split()
  v = [int(x) for x in v[1:]]
  nd[i] = v
  oin[v[2]] = oin[v[3]] = oout[v[0]] = i
  if v[1]: 
      oout[v[1]] = i
sz[1] = M

rec(1)
for _ in range(Q):
  x,k = map(int,input().split())
  if k > sz[x]: 
      print('none')
      continue
  while x != 1:
    v = nd[oout[x]]
    if v[1]:
        if k <= sz[v[0]]:
            x = v[0]
        else:
            x = v[1]
            k -= sz[v[0]]
    else:
        d = sz[v[0]] + 1>>1
        if k <= d:
            x = v[2]
            k = k<<1|1
        else:
            x,v[3]
            k = k-d<<1
  print(k)
