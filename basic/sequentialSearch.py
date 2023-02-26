# 순차탐색으로 특정 값의 위치 찾기

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i

    return -1

v = [17, 92, 18 ,33, 58, 7, 33, 42]
print(search_list(v ,18))
print(search_list(v ,42))

def search_name(i, no, na):
    l = len(no)
    stu_no = -1
    for j in range (0, l):
        if i == no[j]:
            return na[j]

no=[39, 14, 67, 105]
na=['justin', 'john', 'mike', 'summer']
print(search_name(67, no, na))