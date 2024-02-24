"""
10
RGGBRGRGBR
1

15
brgbrgrbgrbgrbg
4
"""

N = int(input())
s = input()
s = s.lower()

c = 0
gC = 0
rC = 0
for i in range(N):
    j = s[i]
    if j == "r":
        rC += 1
    elif rC > 0:
        if j == "g":
            gC += 1
            if (gC > 1):
                rC -= 1
                if rC > 0:
                    gC = 1
                else:
                    gC = 0
                    rC = 0
        elif j == "b" and gC == 1:
            c += 1
print(c)
