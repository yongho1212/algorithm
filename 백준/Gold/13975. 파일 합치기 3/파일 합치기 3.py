
import sys
import heapq

input = sys.stdin.readline
n = int(input())
for j in range(n):
    x = int(input())
    ans = 0
    arr = list(map(int, input().split()))
    q = []
    for i in arr:
        heapq.heappush(q, i)

    while len(q) > 1:
        hap = heapq.heappop(q) + heapq.heappop(q)
        ans += hap
        heapq.heappush(q, hap)
    print(ans)