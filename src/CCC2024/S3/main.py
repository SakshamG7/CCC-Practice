N = int(input())
a = list(map(int, input().split(" ")))
o = list(map(int, input().split(" ")))
sO = set(o)
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

2 2 2 2 2 1 2 1 L
2 1 1 1 1 1 2 1 L
2 1 1 2 2 2 2 1 L
2 1 1 2 1 1 1 1 L
"""


def pivotCheck(arr: list, a: int, b:int):
    for x in range(o):
        for y in range(a)



def recall(arr: list, K: int, ins: str):
    global com

    sArr = set(arr)
    for i in sO:
        if i not in sArr:
            return

    # print(arr)
    add = True
    index = 0
    for i in com:
        if arr == i:
            add = False
            break
        index += 1
    if add:
        com.append([arr.copy(), set(), set()])
        index = len(com) - 1
        # print(index)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            rS = f"\nR {i} {j}"
            c = len(com[index][1])
            com[index][1].add(rS)
            if len(com[index][1]) - c != 0:
                swipes(arr.copy(), K + 1, ins + rS)

            lS = f"\nL {i} {j}"
            c = len(com[index][2])
            com[index][2].add(lS)
            if len(com[index][2]) - c != 0:
                swipes(arr.copy(), K + 1, ins + lS)


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
    a_ = int(curIns[1])
    b = int(curIns[2])
    if c == "R":
        # print(arr, a_, b)
        for i in range(a_ + 1, b + 1):
            arr[i] = arr[i - 1]
        # print(arr, a_, b, "\n")
    elif c == "L":
        # print(arr, a_, b)
        for i in range(b, a):
            arr[i] = arr[a_]
        # print(arr, a_, b, "\n")

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
        # if (a, o) != ([1, 2], [2, 1]):
        #     print(ao, o)
