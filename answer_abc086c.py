def solve():
  N = int(input())

  pt, px, py = 0, 0, 0

  for i in range(N):
    T, X, Y = map(int, input().split())

    t, x, y = T-pt, abs(X-px), abs(Y-py)

    if t < x + y:
      return False

    if t % 2 != (x + y) % 2:
      return False
    
    pt, px, py = t, x, y

  return True

print("Yes" if solve() else "No")