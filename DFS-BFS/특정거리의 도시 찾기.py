from collections import deque

n, m, k, x = map(int, input().split())
arr = [[0]*n for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

print(arr)

distance = [-1] * (n+1)
distance[x] = 0


q = deque([x])
while q:
    now = q.popleft()
    # 현재 노드와 연결된점들
    for nxt_node in arr[now]:
        # 아직 가지 않은 점이라면
        if distance[nxt_node] == -1:
            #다음 노드까지의 거리를 현재 노드거리 + 1
            distance[nxt_node] = distance[now] + 1
            # 다음 노드 큐에 추가
            q.append(nxt_node)

check = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
#
# from collections import deque
# n, m, k, x = map(int, input().split())
# arr = [[0]*n for _ in range(n)]
# for _ in range(n):
#     a, b = map(lambda x:x-1, map(int, input().split()))
#     arr[a][b] = arr[b][a] = 1
#
# dist = [-1] * (n+1)
# dist[x] = 0
#
# q = deque([x])
# while q:
#     now = q.popleft()
#     for nxt_node in arr[now]:
#         print(nxt_node)
#         if dist[nxt_node] == -1:
#             dist[nxt_node] = dist[now] + 1
#             q.append(nxt_node)
#
# check = False
# for i in range(n+1):
#     if dist[i] == k:
#         print(i)
#         check = True
#
# if check == False:
#     print(-1)