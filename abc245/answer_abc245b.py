n=int(input())
a=list(map(int,input().split()))

for i in range(n+1):
    if i not in a:
        print(i)
        break