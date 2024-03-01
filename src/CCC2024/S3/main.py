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

6
1 2 3 4 5 6
1 1 4 5 5 5
YES
4
R 0 1
L 2 3
L 3 4
R 4 5
"""

N = int(input())
a = list(map(int, input().split(" ")))
o = list(map(int, input().split(" ")))
# N = 8
# a = [1, 1, 1, 1, 2, 1, 2, 1]
# o = [2, 1, 1, 2, 1, 1, 1, 1]
# N = 3
# a = [3, 1, 2]
# o = [3, 1, 1]
# print(N, a, o, sep="\n")
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
    oldXL = None
    oldXR = None
    for x in range(len(o)):
        for y in range(index, len(cArr)):
            if o[x] == cArr[y]:
                index = y
                if x < cArrIndex[y] and oldXL != o[x]:
                    oldXL = o[x]
                    ins.append(f"L {x} {cArrIndex[y]}")
                    k += 1
                # TODO: Fix the right swipe to be more efficient, similar to the left swipe
                # fails on test case (a = [7, 5, 1, 8, 7, 4, 7, 5], o = [7, 7, 5, 5, 5, 5, 5, 5])
                elif x > cArrIndex[y] and oldXR != o[x]:
                    oldXR = o[x]
                    ins.append(f"R {cArrIndex[y]} {x}")
                    k += 1
            break

    solved = (([1, 2], [2, 2]), ([3, 2], [3, 3]), ([7, 7, 1, 4, 3, 8, 3, 1], [7, 1, 4, 4, 3, 8, 8, 1]),)
    if (a, o) not in solved:
        print(N, (a, o), sep="\n")

    print("YES", k, sep="\n")
    for i in range(k):
        print(ins[i], end="")
        if i != k - 1:
            print()

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


if not ex:
    pivotSolve(a.copy())
