def solution(s):
    stk = []
    for i in s:
        stk.append(i)
        if len(stk) >= 2 and stk[-1] == stk[-2]:
            stk.pop()
            stk.pop()
    if stk:
        return 0
    else :
        return 1