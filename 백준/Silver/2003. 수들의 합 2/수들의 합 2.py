import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 0
cnt = 0

while j < N:
    temp_sum = sum(arr[i:j + 1])

    if temp_sum == M:
        cnt += 1
        i += 1
    elif temp_sum < M:
        j += 1
    else:
        i += 1

print(cnt)
