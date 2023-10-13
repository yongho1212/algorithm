import sys
N,r,c= map(int, sys.stdin.readline().split())


def sol(N, r, c):
    if N == 0:
        return 0

    return 2 * (r % 2) + (c % 2) + 4 * sol(N - 1, int(r / 2), int(c / 2))

print(sol(N, r, c))




#  다음 위치를 선택하는 알고리즘이 필요함
#  00 => 01 => 10 => 11 => 02 => 03 => 21 => 31
# N을 받아와서 특정 조건에 다르면 위치 이동 그전엔 z모양으로

## 분할정복 / 재귀
