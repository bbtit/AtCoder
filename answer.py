# yesと表示して処理終了
def Yes():
  print("Yes")
  exit(0)

# 入力受付
N = int(input())
X, Y = [], []
for _ in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
S = input()

# right_min : キーを k としたとき、y=k でありかつ右を向いている人のうち最も x 座標が小さい人 (右を向いてる人用の辞書 y座標:最小のx座標) 右向き最小
# left_max : キーを k としたとき、y=k でありかつ左を向いている人のうち最も x 座標が大きい人 (左を向いている人用の辞書 y座標:最大のx座標) 左向き最大
right_min, left_max = dict(), dict()


for i in range(N):

    if S[i] == 'R':
        # もし辞書にあるy座標なら比較して小さい方のx座標を登録
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]])
        # もし辞書にないy座標ならひとまず登録
        else:
            right_min[Y[i]] = X[i]

    # if S[i] == 'L'
    else:
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]

    # y座標が辞書に登録されていて、左向き最大よりもx座標が小さくて右向き→衝突
    if S[i] == 'R':
        if Y[i] in left_max and X[i] < left_max[Y[i]]:
            Yes()

    # if S[i] == 'L'
    # y座標が辞書に登録されていて、右向き最小よりもx座標が大きくて左向き→衝突
    else:
        if Y[i] in right_min and right_min[Y[i]] < X[i]:
            Yes()

print("No")