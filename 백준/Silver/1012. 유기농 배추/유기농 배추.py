from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    ans = []


    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    def dfs(i,j):
        cnt = 1
        q = deque()
        q.append([i,j])
        visited[i][j] = True
        while q:
            y, x = q.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<= ny < n and 0<= nx < m:
                    if graph[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append([ny,nx])
                        cnt += 1
        return cnt





    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                pick = dfs(i,j)
                ans.append(pick)


    print(len(ans))
