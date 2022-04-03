n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

aj=1
bj=1

for i in range(n-1):
    next_a=0
    next_b=0

    if aj==1:
        if abs(a[i]-a[i+1])<=k:
            next_a=1
        if abs(a[i]-b[i+1])<=k:
            next_b=1
    
        


    if bj==1:
        if abs(b[i]-b[i+1])<=k:
            next_b=1
        if abs(b[i]-a[i+1])<=k:
            next_a=1

    aj=next_a
    bj=next_b

    if(aj==bj==0):
        print("No")
        break

if(aj==1 or bj==1):
        print("Yes")