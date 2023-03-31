from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

N, M = map(int, input().split())
arr = [input() for _ in range(N)]


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M
# (0,0) => (N-1,M-1)
# BFS

def BFS():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True
    q = deque()
    q.append((0, 0, 1))
    while q:
        y, x, d= q.popleft()
        if y == M - 1 and x == N - 1:
            return d
        nd = d + 1
        for k in range(4):
            ny = x + dy[k]
            nx = y + dx[k]
            if is_valid_coord(ny,nx) and not chk[ny][nx] and arr[ny][nx] == "1":
                chk[ny][nx] = True
                q.append((ny,nx, nd))
print(BFS())