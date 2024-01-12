
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nodes = [0] * N
mx = 0
for i in range(N):
  ch, x, y, z = input().split()
  x, y, z = map(int, [x, y, z])
  mx = max(mx, x, y, z)
  if ch == 'S':
      nodes[i] = [x, 0, y, z]
  else:
      nodes[i] = [x, y, z, 0]

indexes_in = [0] * (mx+1)
indexes_out = [0] * (mx+1)
for i in range(N):
  indexes_in[nodes[i][0]] = indexes_in[nodes[i][1]] = indexes_out[nodes[i][2]] = indexes_out[nodes[i][3]] = i

sizes = [-1] * (mx+1)
sizes[0] = 0
def rec(x, sz):
  sizes[x] = sz
  if indexes_in[x] == 0:
      return
  v = nodes[indexes_in[x]]
  if sizes[v[0]] == -1 and sizes[v[1]] == -1:
      return
  if v[1]:
      rec(v[2], sizes[v[0]]+sizes[v[1]])
  else:
      rec(v[2], (sizes[v[0]]+1)//2)
      rec(v[3], sizes[v[0]]//2)

rec(1, M)
for i in range(2, mx+1):
  if not indexes_out[i]:
      rec(i, 0)

for _ in range(Q):
  x, k = map(int, input().split())
  if k > sizes[x]:
      print("none")
      continue
  while x != 1:
      v = nodes[indexes_out[x]]
      if v[1]:
          sz = min(sizes[v[0]], sizes[v[1]])
          if k <= 2 * sz:
              x = v[not k % 2]
              k = (k+1) // 2
          else:
              x = v[sizes[v[1]] > sizes[v[0]]]
              k -= sz
      else:
          k = 2 * k - (v[2] == x)
          x = v[0]
  print(k)
