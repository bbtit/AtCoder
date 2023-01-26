import math

n,k = map(int,input().split())
a=list(map(int,input().split()))
coord=[list(map(int,input().split())) for _ in range(n)]
output=0

for i,j in enumerate(coord):
  minlen=10000000
  if i+1 in a:
    pass
  else:
    for k in a:
      dist=math.sqrt((coord[k-1][0]-j[0])**2+(coord[k-1][1]-j[1])**2)
      minlen=min(dist,minlen)
    output=max(minlen,output)

print(output)