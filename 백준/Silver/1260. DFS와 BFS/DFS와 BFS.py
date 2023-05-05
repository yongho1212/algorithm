from collections import deque

n, m, v = map(int, input().split())

adj = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n + 1)
visited2 = [False] * (n + 1)


for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[a].sort()
    adj[b].append(a)
    adj[b].sort()


dfsres = ''
def dfs(adj, num, visited):
    global dfsres
    dfsres += str(num)+" "
    visited[num] = True

    for i in adj[num]:
        if not visited[i]:
            dfs(adj, i, visited)
    return dfsres
def bfs(num):
    q = deque()
    q.append(num)
    visited2[num] = True
    arr = str(num)+ " "
    while q:
        a = q.popleft()
        for i in adj[a]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True
                arr +=  str(i)+" "
    return arr




print(dfs(adj, v, visited))
print(bfs(v))