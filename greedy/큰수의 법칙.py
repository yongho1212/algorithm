# # 큰수의 법칙 = 다양한 수로 이루어진 배열이 있을 ㅇ때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
#
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# # n개의 자연수를 총m번 더해고 한숫자는 k번 반복할 수있다. 이 때 최대 수를 구하라
# data.sort(reverse=True)
# most = data[0]
# second = data[1]
#
# result = 0
# while True :
#     for i in range(k):
#         if m == 0 :
#             break
#         result += most
#         m -= 1
#
#     if m == 0 :
#         break
#     result += second
#     m -= 1
#
# print(result)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

print(result)