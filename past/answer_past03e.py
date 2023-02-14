# グラフ
n, m, q = map(int,input().split())

g = [[] for i in range(n)]

for i in range(m):
  u, v = map(int,input().split())

  u -= 1
  v -= 1

  g[u].append(v)
  g[v].append(u)

col = list(map(int,input().split()))

for i in range(q):
  t, x, *y = map(int, input().split())

  x -= 1

  print(col[x])

  if t == 1:
    for v in g[x]:
      col[v] = col[x]

  else:
    col[x] = y[0]