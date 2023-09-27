import sys

a, b, c = map(int, sys.stdin.readline().split())


def sol(a, n):
    if n == 1:
        return a % c
    else:
        tmp = sol(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(sol(a, b))