# 方針：総白マス数から最短経路白マス数を引いた数が黒く塗れるマスの数
# 下方向がx正方向、右方向がy正方向

from queue import Queue

DX = [1,0,-1,0]
DY = [0,1,0,-1]

H,W = map(int,input().split())

S = [ input() for i in range(H)]

# キューを準備
que = Queue()
# 始点から各座標までの距離を記録
dist = [[-1]*W for _ in range(H)]

# 幅優先探索のための準備
que.put((0,0))
dist[0][0] = 0

while not que.empty():
  x,y = que.get()

  for dx,dy in zip(DX,DY):
    x2,y2 = x+dx,y+dy

    # 範囲外ならスキップ
    if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W:
      continue

    # 黒マスならスキップ
    if S[x2][y2] == "#":
      continue

    # すでに訪問済みならスキップ
    if dist[x2][y2] != -1:
      continue

    # どれにも当てはまらなかったキューに入れて、距離は+1
    que.put((x2,y2))
    dist[x2][y2] = dist[x][y] + 1

# 総白マス数
white = sum(line.count('.') for line in S)

# 右下に辿り着く場合
if dist[H-1][W-1] != -1:
  print(white - dist[H-1][W-1] -1)

else:
  print(-1)
