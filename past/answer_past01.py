# 区間分割・連長圧縮
s = input()

i = 0

word = []

while i < len(s):
  j = i + 1

  while j < len(s) and s[j].islower():
    j += 1

  word.append(s[ i : j+1 ])

  i = j + 1

word.sort( key = str.lower)

print("".join(word))