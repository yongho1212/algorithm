# 값을 입력받습니다.
t = int(input())  # 테스트 케이스의 개수
n_list = []  # n 값을 저장할 리스트

# n 값을 입력받습니다.
for i in range(t):
    n_list.append(int(input()))

# dp 테이블을 초기화합니다.
dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4  # n이 1,2,3일 때의 방법의 수를 미리 저장합니다.

# n이 4 이상일 때의 방법의 수를 계산합니다.
for i in range(4, 11):

    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 각 n 값에 대한 방법의 수를 출력합니다.
for n in n_list:
    print(dp[n])
