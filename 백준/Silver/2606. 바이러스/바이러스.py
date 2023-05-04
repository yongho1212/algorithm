n = int(input())
m = int(input())

adj = [[]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


cnt = 0
def dfs(adj, num, visited):
    
    visited[num] = True
    global cnt;
    cnt += 1

    for i in adj[num]:
        if not visited[i]:
            dfs(adj, i, visited)
    return cnt

print (dfs(adj, 1, visited) - 1)