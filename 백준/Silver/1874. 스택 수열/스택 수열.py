from collections import deque

n = int(input())

stk = deque()
for i in range(n):
    a = int(input())
    stk.append(a)

arr = []
prcc = []
possible = True

for i in range(1,n+1):
    arr.append(i)
    prcc.append("+")
    while stk and len(arr) > 0 and stk[0] == arr[-1]:
        arr.pop()
        stk.popleft()
        prcc.append("-")

if stk:
    possible = False
    prcc = ["NO"]

if possible:
    for op in prcc:
        print(op)
else:
    print("NO")