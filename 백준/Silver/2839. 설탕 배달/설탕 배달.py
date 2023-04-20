num = int(input())
cnt = 0

while num >= 0:
    # 5로 나누어 떨어지면
    if num % 5 == 0:
        # 5로 나눈 몫 더하기
        cnt += int(num // 5)
        print(cnt)
        break
    # 아닌 경우는 3씩 빼기
    num -= 3
    cnt += 1

else:
    print(-1)