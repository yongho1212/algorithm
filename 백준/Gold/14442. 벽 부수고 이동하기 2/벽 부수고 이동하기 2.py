from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

n, m, k = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n) ]


def bfs(y, x, cnt):
    q = deque()
    global k
    q.append([y, x, k, cnt])
    visited[y][x][k] = True

    while q:
        y, x, brw, cnt = q.popleft()

        if [y, x] == [n - 1, m - 1]:
            return cnt


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m :
                if graph[ny][nx] == 0 and not visited[ny][nx][brw]:
                    q.append((ny, nx, brw, cnt + 1))
                    visited[ny][nx][brw] = True

                elif graph[ny][nx] == 1 and brw > 0 and not visited[ny][nx][brw-1]:
                    q.append((ny, nx, brw-1, cnt + 1))
                    visited[ny][nx][brw-1] = True


    return -1


print(bfs(0, 0, 1))
