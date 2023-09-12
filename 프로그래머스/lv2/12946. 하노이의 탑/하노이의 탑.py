def solution(n):
    return hanoi(n, 1, 3)

def hanoi(n, a, b): # n개, a -> b
    if n == 0: return []
    return hanoi(n-1, a, 6-(a+b))+[[a, b]]+hanoi(n-1, 6-(a+b), b)