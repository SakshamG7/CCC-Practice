N = int(input())
a = list(map(int, input().split(" ")))
o = list(map(int, input().split(" ")))
imp = True
ex = False

if a == o:
    print("YES\n0", end="")
    ex = True
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


def recall(arr: list, K: int, ins: str):
    global com
    # print(arr)
    add = True
    index = 0
    for i in com:
        if arr == i:
            add = False
            break
        index += 1
    if add:
        com.append([arr.copy(), set()])
        index = len(com) - 1
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            if j > i:
                c = len(com[index][1])
                rS = f"\nR {i} {j}"
                com[index][1].add(rS)

                c2 = len(com[index][1])
                if c2 - c != 0:
                    c = c2
                    swipes(arr.copy(), K + 1, ins + rS)

                lS = f"\nL {j} {i}"
                com[index][1].add(rS)

                c2 = len(com[index][1])
                if c2 - c != 0:
                    swipes(arr.copy(), K + 1, ins + lS)
            else:
                continue


def swipes(arr: list, K: int, ins: str):
    global a, imp
    arrC = arr.copy()
    if K > N:
        return
    elif K == 0:
        recall(arr, K, ins)
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

    if arr == arrC:
        return

    if arr == o:
        a = arr
        imp = False
        print("YES\n" + str(K) + ins, end="")
        return
    recall(arr, K, ins)


if not ex:
    swipes(a.copy(), 0, "")
    if imp:
        print("NO")
        if (a, o) != ([1, 2], [2, 1]):
            print(a, o)
