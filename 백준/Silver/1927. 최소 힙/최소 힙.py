import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(arr, x)
    else:
        if arr:
            print(heapq.heappop(arr))
        else: print(0)