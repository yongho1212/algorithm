import sys
input = sys.stdin.readline

# input 받기
n, m, r = map(int, input().split())

# 인접 행렬 만들기
arr = [[] for _ in range(n+1)]

#간선 인접행렬에 넣기
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# 시작노드로 부터의 거리 만들기
dist = [0]*(n+1)

cnt = 1

print(arr)

# dfs
def dfs(v): # v 정점집 e 간선 집합 r 시작 정점
    global cnt
    dist[v] = cnt
    arr[v].sort()
    for nxt in arr[v]:
        if dist[nxt] == 0:
            cnt += 1
            dfs(nxt)
dfs(r)
for i in range(1, n+1):
    print(dist[i])
#
# n, m, r = map(int, input().split())
# arr = [[] for _ in range(n+1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     arr[u].append(v)
#     arr[v].append(u)
#
# visited = [0]*(n+1)
# print(arr, visited)
# cnt = 1
# def dfs(v):
#     global cnt
#     visited[v] = cnt
#     arr[v].sort()
#     for nxt in arr[v]:
#         if visited[nxt] == 0 :
#             cnt += 1
#             dfs(nxt)
#
# dfs(r)
# print(visited)
# for i in range(n+1):
#     print(visited[i])