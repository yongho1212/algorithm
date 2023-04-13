import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    if x != 0:
       heapq.heappush(arr, [abs(x), x])
    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
