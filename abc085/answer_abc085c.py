N, Y = map(int,input().split())

ares, bres, cres = -1, -1, -1

for a in range(N+1):
  for b in range(N+1):
    c = N - a -b

    if c < 0:
      continue

    if a + b + c == N and 10000*a + 5000*b +1000*c == Y:
      ares, bres, cres = a, b, c

print(ares, bres, cres)