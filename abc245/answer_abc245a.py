a,b,c,d = map(int,input().split())
if a<c:
    print("Takahashi")
elif a>c:
    print("Aoki")
elif a==c:
    if b<=d:
        print("Takahashi")
    else:
        print("Aoki")