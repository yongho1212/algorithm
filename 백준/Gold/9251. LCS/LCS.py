S1 = list(input())
S2 = list(input())
len1 = len(S1)
len2 = len(S2)
dp = [[0]*(len2 + 1) for _ in range(len1+1)]


for i in range(1,len1 + 1):
    for j in range(1,len2 + 1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # ex dp[4][5] => 이미 ACA가 dp[3][5]에 포함되어있다.
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])


print(dp[len1][len2])