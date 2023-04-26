# 그림의 갯수
# 가장큰 그림의 크기

# visited

# 2차원 배열을 순회하면서 1이면 멈추고 BFS돌면서 크기를 파악.

from collections import deque

n, m = map(int, input().split())

visited = [[False] * m for _ in range (n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

each = 0
result = []

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny <m:
                if not visited [nx][ny]  and graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return cnt

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and visited[x][y] == False:
            pic = bfs(x,y)
            result.append(pic)

if not result:
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))

