import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# i부터 j까지의 합을 구하라
dp = [0] * (n + 1)
dp[0] = arr[0]

# 프리픽스 합 배열 계산
for i in range(1, n):
    dp[i] = dp[i - 1] + arr[i]

# i 부터 j까지의 합 구하는 쿼리 실행
for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        print(arr[a - 1])
    else:
        print(dp[b - 1] - (dp[a - 2] if a - 2 >= 0 else 0))
