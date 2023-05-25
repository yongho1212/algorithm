from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[]*n for _ in range(n+1)]
distance = [-1] * (n+1)
distance[a] = 0

for i in range(m):
    q,w = map(int, input().split())
    graph[q].append(w)
    graph[w].append(q)
# print(graph)
def BFS(start):
    q = deque()
    q.append(start)
    while q:
        curr = q.popleft()
        if curr == b:
            return distance[curr]
            break
        for i in graph[curr]:
            
            if distance[i] == -1:
                distance[i] = distance[curr] + 1
                q.append(i)
    return -1

print(BFS(a))