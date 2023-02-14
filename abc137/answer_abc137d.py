from heapq import heappush, heappop

N, M = map(int,input().split())

# 支払日と報酬をまとめた二次元配列を作成
AtoB = [[] for _ in range(M + 1)]

for _ in range(N):
  A, B = map(int,input().split())

  if A > M:
    continue

  AtoB[A].append(B)

result = 0

que = []

# M-1日目→0日目の順で仕事を見ていく
# つまり，AtoB[0]から順に見ていく
for Bs in AtoB:
  for B in Bs:
    # pythonのヒープは小さい順に埋まる．大きい順にするためにーをつける
    heappush(que,-B)

  if que:
    result -= heappop(que)

print(result)