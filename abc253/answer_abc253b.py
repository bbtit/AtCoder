h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]
l=[]

for i in range(h):
  for j in range(w):
    if s[i][j]=="o":
      l.append((i,j))

step_num=abs(l[0][0]-l[1][0])+abs(l[0][1]-l[1][1])
print(step_num)