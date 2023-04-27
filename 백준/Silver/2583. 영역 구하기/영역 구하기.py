from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

n, m, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = []

for _ in range(k):
    a,b,c,d = map(int, input().split())
    for j in range(b,d):
        for i in range(a,c):
            graph[j][i] = 1

def bfs(y,x):
    cnt = 1
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < n and 0<= nx < m:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    cnt += 1
    return cnt



for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            pick = bfs(i,j)
            ans.append(pick)

ans.sort()
if not ans:
    print("0 0 0")
else:
    stra = ''
    for i in ans:
        stra += str(i) + ' '
    print(len(ans))
    print(stra)

