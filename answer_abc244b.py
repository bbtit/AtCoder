n=int(input())
t=input()

x,y = 0,0
dx=[1,0,-1,0]
dy=[0,-1,0,1]
d=0

for c in t:
    if c=='S':
        x+=dx[d]
        y+=dy[d]
    
    else:
        d=(d+1)%4

print(str(x) + ' ' + str(y))