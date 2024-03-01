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
YES
4
L 4 0
L 5 1
L 6 3
L 7 4
"""

# N = int(input())
# a = list(map(int, input().split(" ")))
# o = list(map(int, input().split(" ")))
N = 8
a = [1, 1, 1, 1, 2, 1, 2, 1]
o = [2, 1, 1, 2, 1, 1, 1, 1]
N = 3
a = [3, 1, 2]
o = [3, 1, 1]
print(N, a, o, sep="\n")
imp = True
ex = False

if a == o:
    print("YES\n0", end="")
    ex = True
com = []

cO = [o[0]]
cOIndex = [0]
for i in range(N):
    if o[i] != cO[-1]:
        cO.append(o[i])
        cOIndex.append(i)


def pivotSolve(arr: list):
    if pivotCheck(arr) is False:
        print("NO")
        return
    k = 0
    ins = []

    # compress arr
    cArr = [arr[0]]
    cArrIndex = [0]
    for i in range(len(arr)):
        if arr[i] != cArr[-1]:
            cArr.append(arr[i])
            cArrIndex.append(i)

    index = 0
    index2 = len(cArr)
    for x in range(len(o)):
        for y in range(index, len(cArr)):
            if o[x] == cArr[y]:
                index = y
                if x < cArrIndex[y]:
                    ins.append(f"L {cArrIndex[y]} {x}")
                    k += 1
                elif x > cArrIndex[y]:
                    ins.append(f"R {cArrIndex[y]} {x}")
                    k += 1
                break
            elif y == N - 1:
                return False

    print("YES", k, sep="\n")
    for i in ins:
        print(i)

    return k, ins


def pivotCheck(arr: list) -> bool:
    index = 0
    for x in range(len(cO)):
        for y in range(index, N):
            if cO[x] == arr[y]:
                index = y
                break
            elif y == N - 1:
                return False
    return True


def recall(arr: list, K: int, ins: list):
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

            rS = f"R {i} {j}"
            c = len(com[index][1])
            com[index][1].add(rS)
            if len(com[index][1]) - c != 0:
                swipes(arr.copy(), K + 1, ins + [rS])

            lS = f"L {i} {j}"
            c = len(com[index][2])
            com[index][2].add(lS)
            if len(com[index][2]) - c != 0:
                swipes(arr.copy(), K + 1, ins + [lS])


def swipes(arr: list, K: int, ins: list):
    global a, imp
    arrC = arr.copy()

    if K > N:
        return
    elif K == 0:
        recall(arr, K, ins)
        return
    if a == o:
        return

    curIns = ins[-1].split(" ")
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
        print("YES\n" + str(K))
        for i in ins:
            print(i)
        return
    recall(arr, K, ins)


if not ex:
    # swipes(a.copy(), 0, [])
    pivotSolve(a.copy())
    # if imp:
    #     print("NO")
