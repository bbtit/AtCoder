n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans1=0
ans2=0

for i in range(n):
    if a[i]==b[i]:
        ans1+=1
    if a[i] in b:
        ans2+=1

print(str(ans1)+"\n"+str(ans2-ans1))