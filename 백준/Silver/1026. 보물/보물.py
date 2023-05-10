n= int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort(reverse=True)
ans = 0
for i in range(len(l1)):
    ans += l1[i] * l2[i]
print(ans)