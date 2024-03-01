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

2 2 2 2 2 1 2 1 L
2 1 1 1 1 1 2 1 L
2 1 1 2 2 2 2 1 L
2 1 1 2 1 1 1 1 L
"""


def pivotCheck(arr: list):
    index = 0
    for x in range(N):
        for y in range(index, N):
            if o[x] == arr[y]:
                index = y
                break
            elif y == N - 1:
                return False

    return True


def recall(arr: list, K: int, ins: str):
    global com

    if pivotCheck(arr) is False:
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
        for i in range(a_ + 1, b + 1):
            arr[i] = arr[i - 1]
    elif c == "L":
        for i in range(b, a_):
            arr[i] = arr[a_]

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
