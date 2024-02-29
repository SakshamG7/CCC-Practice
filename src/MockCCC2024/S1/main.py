N, K = map(int, input().split(" "))
mIn = input()
m = []

for i in mIn:
    m.append(int(i))

for i in range(N-1):
    if m[i] == 1 and m[i+1] == 1:
        m[i] = 0

mC = []
temp = 0
count = 0
for i in m:
    if i == 0:
        temp += 1
    else:
        mC.append(temp)
        temp = 0
    count += i

m = None

if (len(mC) > 1):
    mC.pop(0)
mC.sort()
for i in mC:
    if i <= K:
        count -= 1
        K -= i

if count <= 0 and K > 0:
    count = 1

print(count)
