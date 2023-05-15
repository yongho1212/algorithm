from collections import deque

def solution(prices):
    q = deque(prices)
    ans = []
    
    while q:
        price = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if price > i:
                break
        ans.append(sec)
    return ans