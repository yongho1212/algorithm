a,b,c = map(int, input().split())
arr = [a, b, c]
arr.sort();
ans = 0
if arr[0] != arr[1] != arr[2]:
    ans = arr[2] * 100
elif arr[0] == arr[1] and arr[1] != arr[2] or arr[0] != arr[1] and arr[1] == arr[2]:
    ans = 1000 + arr[1] * 100
elif arr[0] == arr[1] == arr[2]:
    ans = 10000 + arr[1] * 1000
print(ans)