n = int(input())
st = sorted(list(map(int, input().split())))
m = int(input())
sa = list(map(int, input().split()))

def binarySearch(arr, val):
    left = binaryLower(arr, val)
    right = binaryUpper(arr, val)
    return left, right

def binaryLower(arr, val):
    l, r = 0, len(arr)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] >= val:
            r = mid
        elif arr[mid] < val:
            l = mid + 1
    return l

def binaryUpper(arr, val):
    l, r = 0, len(arr)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] <= val:
            l = mid + 1
        elif arr[mid] > val:
            r = mid
    return l

for i in sa:
    l, r = binarySearch(st, i)
    print(r-l, end=' ')
