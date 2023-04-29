
from collections import deque

m,n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# while q를 한 후 전체 검색해서 0이 있으면 -1 없으면 cnt
# 양방향 탐색을 해야함. 근데 보통 bfs를 돌면 두개이상씩

#1이 2개 이상인경우 , 어차피 1로 퍼져나가면 똑같은 타입이다. 그럼 둘다 큐에 집어 넣자.
# (0,0,0)


tmt = []

def bfs():
    q = deque()
    for k in tmt:
        y ,x, cnt = k
        q.append([y,x,cnt])
        visited[y][x] = True

    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    q.append([ny, nx, cnt + 1])
                    visited[ny][nx] = True
                    graph[ny][nx] =1

    for row in graph:
        if 0 in row:
            return -1
    return cnt



for a in range(n):
    for b in range(m):

        if graph[a][b] == 1:
            tmt.append([a,b,0])


print(bfs())