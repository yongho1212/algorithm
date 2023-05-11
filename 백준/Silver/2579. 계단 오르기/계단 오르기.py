# 입력받기
n = int(input())
stairs = [0] # 0번째 계단 초기화
for i in range(n):
    stairs.append(int(input()))

# dp 배열 초기화 (계단 0번째는 0점이므로 0으로 초기화 한 것)
dp = [0] * (n + 1)
dp[1] = stairs[1] # 1번째 계단까지의 최대 점수

# 계단이 2개 이하인 경우
if n == 1:
    print(dp[1]) # 1개 계단인 경우 1번째 계단까지 밟을 수 있음
elif n == 2:
    print(stairs[1] + stairs[2]) # 2개 계단인 경우 위의 두 가지 방법 중 최댓값을 출력
else:
    dp[2] = stairs[1] + stairs[2] # 2번째 계단까지의 최대 점수
    # 3번째 계단부터 dp 배열 갱신
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    # n번째 계단까지의 최대 점수 출력
    print(dp[n])
