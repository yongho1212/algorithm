# 카운터에서 거스름돈으로 사용할 100, 100, 50, 10짜리가 무한할 때 손님에게 거슬러줘야할 돈이 n원 일 때
# 거슬러 줘야할 최소갯수를 구하라

n = 1670
count = 0
coin_types = [500, 100 ,50, 10]

for i in coin_types:
    count += n // i
    n %= i

print(count)

# 그리디 알고리즘의 정당성
# 해당 문제의 경우 가지고 있는 동전중에서 큰 단위가 항상 작은 단위의 배수 이므로 작은 단위의 동전들을 종합해 다른 해가 나롷 수 없기 때문이다.