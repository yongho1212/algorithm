import sys

input = sys.stdin.readline

n = int(input())
h = dict()

for i in range(n):
    k,v = map(str, input().split())
    if v == "enter":
        h[k] = v
    else :
        del h[k]

ans = sorted(h.keys(), reverse=True)
for i in ans:
    print(i)