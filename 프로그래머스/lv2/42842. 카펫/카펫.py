import math
def solution(brown, yellow):
    ssum = brown + yellow
    for i in range(3, ssum//2 + 1):
        if ssum % i == 0 and i >= 2:
            if (i - 2) * (ssum//i - 2) == yellow:
                
                return [ssum//i, i]