N, M, V = map(int, input().split())

arr = [[0]*N for _ in range(N)]
print(arr)
visited = [False] * N
print(visited)

for i in range(N):
    u, v = map(lambda x: x-1,map(int, input().split()))
    arr[u][v] = arr[v][u] = 1
