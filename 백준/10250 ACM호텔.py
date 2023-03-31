
import math

t = int(input())
ans = []
for i in range(t):
    h, w, n = map(int, input().split())
    f = 0
    r = 0
    if n % h == 0:
        f = h * 100
        r = n // h
    else :
        f = (n%h) *100
        r = n // h +1
    print(f + r)