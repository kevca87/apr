
import sys
sys.setrecursionlimit(100000)

M, N, Q = map(int, input().split())
nodes = [[] for _ in range(1)]
max_numbers = 0
for _ in range(N):
  ch, x, y, z = input().split()
  x, y, z = int(x), int(y), int(z)
  max_numbers = max(max_numbers, x, y, z)
  if ch == 'S':
      nodes.append([x, 0, y, z])
  else:
      nodes.append([x, y, z, 0])

index_in = [0] * (max_numbers+1)
index_out = [0] * (max_numbers+1)
for i in range(1, N+1):
  index_in[nodes[i][0]] = index_in[nodes[i][1]] = index_out[nodes[i][2]] = index_out[nodes[i][3]] = i

node_sizes = [-1] * (max_numbers+1)
node_sizes[0] = 0
def recursive(x, sz):
  node_sizes[x] = sz
  if index_in[x] == 0:
      return
  v = nodes[index_in[x]]
  if node_sizes[v[0]] == -1 or node_sizes[v[1]] == -1:
      return
  if v[1]:
      recursive(v[2], node_sizes[v[0]]+node_sizes[v[1]])
  else:
      recursive(v[2], (node_sizes[v[0]]+1)//2)
      recursive(v[3], node_sizes[v[0]]//2)

recursive(M, 1)
for i in range(2, max_numbers+1):
  if not index_out[i]:
      recursive(i, 0)

for _ in range(Q):
  x, k = map(int, input().split())
  if k > node_sizes[x]:
      print("none")
      continue
  while x != 1:
      v = nodes[index_out[x]]
      if v[1]:
          sz = min(node_sizes[v[0]], node_sizes[v[1]])
          if k <= 2 * sz:
              x = v[not k % 2]
              k = (k+1) // 2
          else:
              x = v[node_sizes[v[1]] > node_sizes[v[0]]]
              k -= sz
      else:
          k = 2 * k - (v[2] == x)
          x = v[0]
  print(k)
