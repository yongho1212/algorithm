from collections import deque

t = int(input())

for _ in range(t):
    s = int(input())
    preLoc = list(map(int, input().split()))
    tarLoc = list(map(int, input().split()))

    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    graph = [[0]*s for _ in range(s)]

    def bfs(y,x):
        q = deque()
        q.append([y,x])

        while q:
            y, x = q.popleft()
            if [y,x] == tarLoc:
                break
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < s and 0 <= nx < s and graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])

        return graph[tarLoc[0]][tarLoc[1]]


    print(bfs(preLoc[0], preLoc[1]))
