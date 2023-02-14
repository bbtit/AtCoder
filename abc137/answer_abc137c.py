# 連想配列 Associative array
from collections import defaultdict

N = int(input())

a = defaultdict(int)

for _ in range(N):
  s = "".join(sorted(input()))
  a[s] += 1

ans = 0
for s in a:
  num = a[s]
  ans += (num*(num-1)//2)

print(ans)