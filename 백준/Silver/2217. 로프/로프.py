n = int(input())
arr = []
for i in range(n):
    t = int(input())
    arr.append(t)

arr.sort()
answer = arr[0]*n

for i in range(1, n):
    answer = max(answer, arr[i] * (n-i))

print(answer)
