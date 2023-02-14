# バケット
N = int(input())

exist = [0] * 101

for _ in range(N):
  d = int(input())
  exist[d] = 1

print(sum(exist))