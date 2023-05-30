n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    # 1자릿수 일 때
    dp[1][i] = 1

# dp[2][1] => 2자릿수 + 앞에 오는 숫자가 1
# dp[2][0] = 0, dp21 ~ dp 28 = 2 dp29 = 1
# dp[3][1] = dp[2][1] + dp[2][0]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j ==9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1000000000)