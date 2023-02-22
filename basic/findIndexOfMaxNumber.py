

def find_num(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

v = [1, 2, 3, 9, 1, 17, 1, 2]
print(find_num(v))

# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 알고리즘
nums = list(map(int, input().split()))
def input_find(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return a[min_idx]

print(input_find(nums))




