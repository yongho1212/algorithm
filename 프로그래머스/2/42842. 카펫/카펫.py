def solution(brown, yellow):
    hap = brown + yellow 
    for x in range(1, hap+1):
        if hap % x == 0:
            y = hap // x
            if (x-2)*(y-2) == yellow:
                return [max(x, y), min(x, y)]