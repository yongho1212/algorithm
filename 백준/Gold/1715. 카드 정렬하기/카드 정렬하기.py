# 입력 받은 값을 리스트에 넣ㄱ

# 1 2 3 4
#
# 3 6 10

import sys
import heapq
input = sys.stdin.readline

# 문제 풀이 시도 1  => 시가 초과
# n = int(input())
#
# arr = [int(input()) for i in range(n)]
#
# ans = 0
# for i in range (n-1):
#     ans += sum(arr[0:i+2])
# print(ans)

cards = []
result = 0
n = int(input())
for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)
    print(result)