# 숫자 10개를 받고 그 수 들을 42로 나눈 나머지 중 다른 수의 갯수
arr = []

for _ in range(10):
    x = int(input())
    arr.append(x%42)

print(len(list(set(arr))))