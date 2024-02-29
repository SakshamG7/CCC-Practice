N = int(input())
a = list(map(int, input().split(" ")))
o = list(map(int, input().split(" ")))
imp = True
ex = False

com = []

"""
3
3 1 2
3 1 1
a = [1, 1, 1, 1, 2, 1, 2, 1]
o = [2, 1, 1, 2, 1, 1, 1, 1]
N = len(a)
8
1 1 1 1 2 1 2 1
2 1 1 2 1 1 1 1
"""

if a == o:
    print("YES\n0",end="")
    ex = True

def swipes(arr: list, K: int, ins: str):
    global a, imp
    if K > N + 1:
        return
    elif K == 0:
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                elif i < j:
                    swipes(arr.copy(), K + 1, ins + f"\nR {i} {j}")
                else:
                    swipes(arr.copy(), K + 1, ins + f"\nL {i} {j}")
        return
    if a == o:
        return
    
    insList = ins.split("\n")
    curIns = insList[-1].split(" ")
    c = curIns[0]
    l = int(curIns[1])
    r = int(curIns[2])
    if c == "R":
        for i in range(l + 1, r + 1):
            arr[i] = arr[i - 1]
    elif c == "L":
        for i in range(r, l):
            arr[i] = arr[i + 1]

    if (arr in com):
        return
    com.append(arr.copy())

    if arr == o:
        a = arr
        imp = False
        print("YES\n" + str(K) + ins, end="")
        return

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif i < j:
                swipes(arr.copy(), K + 1, ins + f"\nR {i} {j}")
            else:
                swipes(arr.copy(), K + 1, ins + f"\nL {i} {j}")

if not ex:
    swipes(a.copy(), 0, "")
    if imp:
        print("NO")
        if (a, o) != ([1, 2], [2, 1]):
            print(a, o)
