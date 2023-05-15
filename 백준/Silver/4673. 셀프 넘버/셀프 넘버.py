# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
numbers = set(range(1,10001))
arr = set()

for i in numbers:
    for j in str(i):
        i += int(j)
    arr.add(i)

ans = numbers - arr

for i in sorted(ans):
    print(i)