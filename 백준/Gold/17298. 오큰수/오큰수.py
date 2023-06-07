n = int(input())
arr = list(map(int, input().split()))

stk = []
ans = [-1]*n

for i in range(n):
    while stk and arr[stk[-1]] < arr[i]:

        ans[stk.pop()] = arr[i]
    stk.append(i)
print(*ans)

# [0, 1]
