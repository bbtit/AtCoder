from itertools import combinations_with_replacement

N,M,Q = map(int,input().split())

a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q

for i in range(Q):
  a[i],b[i],c[i],d[i] = map(int,input().split())

  # 配列のインデックスを示すa[i],b[i]は-1しておく
  a[i] -= 1
  b[i] -= 1

# 数列のスコアを計算する関数
def calc(A):
  score = 0
  for ai,bi,ci,di in zip(a,b,c,d):
    if A[bi] -A[ai] == ci:
      score += di
  return score

max_score = 0

for A in combinations_with_replacement(range(1,M+1),N):
  max_score = max(max_score,calc(A))

print(max_score)