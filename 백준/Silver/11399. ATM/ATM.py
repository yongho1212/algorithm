n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
ans = 0
for i in range(1, len(arr) + 1):
    ans += arr[i-1] * i
print(ans)