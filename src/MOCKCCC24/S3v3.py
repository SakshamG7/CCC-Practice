import sys

N = int(input())
# N = 10**3 - 1
# nums = []
# for i in range(N):
#     nums.append(i + 1)
sys.setrecursionlimit(N*N)
nums = list(map(int, input().split(" ")))

# nums = [1, 2, 1, 3, 3, 2, 1]
# internal output:  2 3
# final output:     3 4
# N = len(nums)

sols = set()
called = set()
sD = -1
def f(nL: list, sP: int, mP: int):
    global sD
    l = nL[:sP]
    r = nL[sP:]
    if len(r) > 1:
        r.pop(0)

    if mP < sP:
        r.append(nL[mP])
        l.pop(mP)
    elif mP > sP:
        l.append(nL[mP])
        r.pop(sP + 1 - mP)

    nD = abs(sum(l) - sum(r))
    if sD == -1:
        sD = nD
    
    if nD <= sD:
        if nD != sD:
            sols.clear()
        sD = nD
        if sP == mP:
            sols.add(f"{sP + 1} -1")
        else:
            sols.add(f"{sP + 1} {mP + 1}")
    # use len and compare before and after of the len after adding item to set if it has changed to be more faster
    if f"{sP + 1} {mP}" not in called and sP + 1 < N:
        f(nL, sP + 1, mP)
        called.add(f"{sP + 1} {mP}")
    if f"{sP} {mP + 1}" not in called and mP + 1 < N:
        f(nL, sP, mP + 1)
        called.add(f"{sP} {mP + 1}")
    if f"{sP + 1} {mP + 1}" not in called and sP + 1 < N and mP + 1 < N:
        f(nL, sP + 1, mP + 1)
        called.add(f"{sP + 1} {mP + 1}")

f(nums, 0, 0)

nSols = []
for i in sols:
    nSols.append(i.split(" "))
    if nSols[-1][-1] == '-1':
        nSols = [nSols[-1]]
        break


nSols.sort()
o = nSols[0]
print(f"{o[0]} {o[1]}")
