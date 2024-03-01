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
L 3 2
L 4 3
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
    oldX = None
    for x in range(len(o)):
        for y in range(index, len(cArr)):
            if o[x] == cArr[y]:
                index = y
                if x < cArrIndex[y] and oldX != o[x]:
                    oldX = o[x]
                    ins.append(f"L {cArrIndex[y]} {x}")
                    k += 1
                elif x > cArrIndex[y]:
                    ins.append(f"R {cArrIndex[y]} {x}")
                    k += 1
                break
            elif y == N - 1 and x == len(o) - 1:
                print("NO")
                return

    solved = (([1, 2], [2, 2]),)
    # if (a, o) not in solved:
    #     print(N, (a, o), sep="\n")

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
