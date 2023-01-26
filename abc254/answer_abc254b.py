n=int(input())
output=[]

# 行
for i in range(n):
  tmp=[]
  # 列
  for j in range(i+1):
    if j==0 or j==i:
      tmp.append(1)
    else:
      tmp.append(output[i-1][j-1]+output[i-1][j])

  output.append(tmp)

for i in output:
  print(" ".join(map(str,i)))