def solution(sizes):
    arr1 = []
    arr2 = []
    for i in sizes:
        i.sort()
        arr1.append(i[0])
        arr2.append(i[1])
    return max(arr1) * max(arr2)