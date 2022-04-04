v,a,b,c,=map(int,input().split())

n=v%(a+b+c)

if n<a or n==0:
    print("F")

elif n<a+b:
    print("M")

else:
    print("T")