from heapq import heappush, heappop

def solution(n, works):
    heap = []

    def maxheap(x):
        for num in x:
            heappush(heap, (-num, num))

    maxheap(works)

    for i in range(n):
        if heap[0][1] == 0:
            break

        priority, value = heappop(heap)
        new_value = value - 1
        new_priority = -new_value
        heappush(heap, (new_priority, new_value))

    ans = 0
    for priority, value in heap:
        ans += value ** 2

    return ans
