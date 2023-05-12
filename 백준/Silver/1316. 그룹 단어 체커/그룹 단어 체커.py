n = int(input())
cnt = 0
for i in range(n):
    arr = list(map(str, input()))

    checked = []
    for i in range(len(arr)):
        if i == 0:
            checked.append(arr[i])
        elif arr[i] != arr[i-1]:
            if arr[i] in checked:
                cnt+= 1
                break
            checked.append(arr[i])
print(n - cnt)



