# N, M = map(int, input().split())

# inputs = f"{N} {M}\n"
# e = False
# if N == 2:
#     print("R")
#     e = True

# roads = [[] for i in range(N + 1)]
# visited = set()
# vi = [] # TODO: REMOVE LATER
# paint = ["G" for i in range(M)]
# c = 0
# prev = True
# for i in range(M):
#     if e:
#         continue
#     u, v = map(int, input().split())
#     inputs += f"{u} {v}\n"
#     temp = True
#     for x in roads:
#         if temp is False:
#             continue
#         if u in x or v in x:
#             temp = False
#             break
#     if temp:
#         paint[c] = "R"
#         visited.add(u)
#         vi.append(u)
#     roads[u].append(v)
#     roads[v].append(u)
#     if not temp:
#         cycle = False
#         for j in roads[v]:
#             if j not in visited:
#                 cycle = True
#                 break
#         for x in roads:
#             if v in x:
#                 cycle = True
#                 break
#         # if cycle is False:
#             if prev:
#                 paint[c] = "B"
#             else:
#                 paint[c] = "R"
#             prev = not prev
#             visited.add(v)
#             vi.append(v)
            
#     c += 1
                    

# # print(roads)

# if not e:
#     for i in paint:
#         print(i, end="")
#     # if inputs.replace("\n", " ") not in ("3 3 2 1 3 1 3 2 "):
#     #     print()
#     #     print(inputs, roads)
#     #     print(vi)
import sys
sys.setrecursionlimit(10**10)
N, M = map(int, input().split())
adj = [[] for i in range(N + 1)]
answer = ["G"] * M

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append((v, i))
    adj[v].append((u, i))

visited = [False] * (N + 1)

def dfs(node, state):
    for neigh, index in adj[node]:
        if visited[neigh]:
            continue
        
        visited[neigh] = True

        if answer[index] == "G":
            if state == 0:
                answer[index] = "R"
            else:
                answer[index] = "B"
            
        dfs(neigh, state ^ 1)
for n in range(1, N + 1):
    if not visited[n]:
        visited[n] = True
        dfs(n, 0)

print("".join(answer))