N, Ra, Rb, K = map(float, input().split(" "))
e = input()

for i in e:
    a = Rb - Ra
    r = a / 400.0
    p = 10 ** r
    p += 1
    s = 1 / p
    if i == 'T':
        se = 0.5
    elif i == 'W':
        se = 1
    else:
        se = 0
    new = (s - se) * K
    RNewA = Ra - new
    RnewB = Rb + new
    print(round(RNewA, 1), round(RnewB, 1))
    Ra = RNewA
    Rb = RnewB
