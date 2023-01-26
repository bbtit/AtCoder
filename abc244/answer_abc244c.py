n=int(input())

a=list(range(1,2*n+2))
while a != []:
    out=a[0]
    print(out,flush=True)
    a.remove(out)

    aoki=int(input())
    if aoki==0:
        exit()
    a.remove(aoki)