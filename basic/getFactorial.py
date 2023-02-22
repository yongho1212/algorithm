
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

print(fact(3))
print(fact(5))

# 재귀함수를 이용한 풀이

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact((3)))

# 문제 1번 1부터 n까지의 합을 재위함수로 만들어라
def sumRecursive(n):
    if n <= 1:
        return 1
    return n + sumRecursive(n-1)

print(sumRecursive(3))
# 숫자 n개중 최댓값을 재뒤함수로 찾아라
def max(x, y):
    if x > y:

        return x

    else:

        return y


def find_max(a,n):
    if n == 1:
        return a[0]
    max_n_1 = find_max(a,n-1)
    if max_n_1 > [n - 1]:
        return max_n_1
    else:
        return a[n-1]

v=[1, 2, 19, 4, 10]
print(find_max(v,len(v)))