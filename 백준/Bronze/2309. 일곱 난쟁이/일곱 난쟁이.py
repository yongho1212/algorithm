from itertools import *

arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
newList = list(combinations(arr,7))
for i in newList:
    if sum(i) == 100:
        for i in sorted(i):
            print(i)
        break

# 7명의 합이 100