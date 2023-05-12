n = int(input())
dp = [0] * (n+1)

# f(n) := 함수f는 n이 주어졌을 때 연산을 사용하는 횟수의 최솟값을 반환한다.
# f(n) = min(f(n), f(n-1)+1)) ;
# dp(n)
# = dp[i] = min(dp[i], dp[i // 3] + 1) if i / 3 == 0
# = dp[i] = min(dp[i], dp[i // 2] + 1) if i / 2 == 0
# = min(dp[i], dp[i-1]+1)  if 그외
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1


    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])