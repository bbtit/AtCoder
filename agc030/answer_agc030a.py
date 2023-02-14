A, B, C = map(int,input().split())

print(B+C if A + B + 1 >= C else B + A + B + 1)