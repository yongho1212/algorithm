# 1. 주식을 산다.
# 2. 원하는 만큼 주식을 판다.
# 3. 아무것도 안한다.

n = int(input())
for _ in range(n):
    d = int(input())
    arr = list(map(int, input().split()))
    val = 0
    max = 0
    # 받은 배열 맨 뒤부터 앞까지 거꾸로 돌면서
    for i in range(len(arr)-1,-1,-1):
        # max값보다 크면 max가 i
        if (arr[i] > max):
            max = arr[i]
        else :
            val += max-arr[i]
    print(val)