from collections import deque

n = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

graph = []
visited = [[False] * n for _ in range(n)]
visitedn = [[False] * n for _ in range(n)]

# 그래프 돌면 서 visited false면 탐색 시작
# dfs돌때는 다음 노드가 같은경우 또는 R orG인 경우 and visited False 인경우만

for _ in range(n):
    graph.append(list(input()))

cntn = 0
cnt = 0
def bfsn(y,x):
    global cntn
    q = deque()
    q.append((y, x))
    cntn += 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < n and 0 <= nx < n:
                if not visitedn[ny][nx] and graph[ny][nx] == graph[y][x]:
                    q.append((ny,nx))
                    visitedn[ny][nx] = True
    return

def bfs(y,x):
    global cnt
    q = deque()
    q.append((y, x))
    cnt += 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < n and 0 <= nx < n:
                if not visited[ny][nx]:
                    if graph[y][x] == "R" or graph[y][x] == "G":
                        if graph[ny][nx] != "B":
                            q.append((ny, nx))
                            visited[ny][nx] = True
                    else:
                        if graph[y][x] == graph[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = True
    return


for i in range(n):
    for j in range(n):
        if visitedn[i][j] == False:
            bfsn(i, j)
        if visited[i][j] == False:
            bfs(i, j)

print(cntn,end=" ")
print(cnt)


