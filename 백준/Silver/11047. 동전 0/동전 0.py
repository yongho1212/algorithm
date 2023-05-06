n, m = map(int, input().split())
arr = []
for i in range(n):
    k = int(input())
    arr.append(k)

arr.reverse()

# 큰것부터 빼서 값이 양수이면 그 해당 수 로 나누고 몫을 반환

cnt = 0


for i in arr:
    cnt += m // i
    m = m % i

print(cnt)