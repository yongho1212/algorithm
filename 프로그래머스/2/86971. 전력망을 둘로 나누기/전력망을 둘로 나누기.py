def solution(n, wires):
    def dfs(x):
        visited[x] = True
        count = 1
        for i in graph[x]:
            if not visited[i]:
                count += dfs(i)
        return count

    max_difference = float('inf')
    
    for i in range(n-1):
        new_list = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n)]
        for a, b in new_list:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

        visited = [False] * n
        components = []
        for j in range(n):
            if not visited[j]:
                component_size = dfs(j)
                components.append(component_size)

        difference = abs(components[0] - components[1])
        max_difference = min(max_difference, difference)

    return max_difference
