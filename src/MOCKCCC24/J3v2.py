"""
10
RGGBRGRGBR
1
---
15
BRGBRGRBGRBGRBG
4
"""

N = int(input())
s = input()
c = 0

def isItRGB(index):
    t1 = index - 1
    t2 = index + 1
    cR = 0
    cB = 0
    while s[t1] != "G":
        if s[t1] == "R":
            cR += 1
        t1 -= 1
        if t1 < 0:
            break
    while s[t2] != "G":
        if s[t2] == "B":
            cB += 1
        t2 += 1
        if t2 > N - 1:
            break

    return cB * cR

for i in range(1, N - 1):
    l = s[i]
    if l == "G":
        c += isItRGB(i)

print(c)
