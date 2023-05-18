n = int(input())

for t in range(n):
    w = int(input())

    # 입력 데이터를 'arr' 리스트에 저장
    arr = [list(map(int, input().split())) for _ in range(2)]

    # 2 x w 크기의 'dp' 리스트를 생성하고 초기화
    dp = [[0] * w for _ in range(2)]

    if w == 1:
        print(max(arr[0][0], arr[1][0]))
    else :

        dp[0][0], dp[1][0] = arr[0][0], arr[1][0]
        dp[0][1], dp[1][1] = arr[1][0] + arr[0][1], arr[0][0] + arr[1][1]

        # 'dp' 리스트를 이용해 최대값 계산
        for i in range(2, w):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]

        # 최대값 출력
        print(max(dp[0][w-1], dp[1][w-1]))
