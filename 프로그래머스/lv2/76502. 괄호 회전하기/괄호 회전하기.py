from collections import deque

def checker(arr):
    stk = []
    pairs = {'}':'{', ']':'[', ')':'('}
    for i in arr:
        if i in pairs.values():
            stk.append(i)
        else:
            if len(stk) == 0 or stk[-1] != pairs[i]:
                return False
            stk.pop()
    return len(stk) == 0

def solution(s):
    lst = deque(s)
    ans = 0
    for _ in range(len(lst)):
        if checker(lst):
            ans += 1
        lst.rotate(-1)
    
    return ans
