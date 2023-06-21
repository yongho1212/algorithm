from collections import deque

def solution(queue1, queue2):
    ans = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2
    limit = (len(queue1)) * 4
    
    if total % 2 != 0:
        return -1
    
    while True:
        if sum1 > sum2:
            num  = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
            ans += 1
        elif sum1 < sum2:
            num  = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
            ans += 1
        else :
            break
        # 무한루프 빠짐 방지 
        if ans == limit:
            ans = -1
            break
        
    return ans