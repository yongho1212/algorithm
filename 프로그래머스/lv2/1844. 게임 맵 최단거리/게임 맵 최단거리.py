from collections import deque

def solution(maps):
    # 세로
    n = len(maps)
    # 가로
    m = len(maps[0]) 
    visited = [[False]*m for _ in range(n)]
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def BFS(y,x,cnt):
        q = deque()
        q.append([y,x, cnt])
        visited[y][x] = True
        while q:
            y, x, cnt = q.popleft()
            if y == n-1 and x == m-1:
                return cnt
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if maps[ny][nx] == 1 and visited[ny][nx] == False:
                        visited[ny][nx] = True
                        q.append([ny,nx,cnt+1])
        return -1
        
    
    return BFS(0,0,1)
    


    
    