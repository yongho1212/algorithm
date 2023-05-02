from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

cnt = 0

def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    size = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = True

                    size += 1
    return size

ans = []

for o in range(n):
    for p in range(n):
        if graph[o][p] == 1 and not visited[o][p]:
            cnt += 1
            ans.append(bfs(o, p))
print(cnt)

for i in sorted(ans):
    print(i)
