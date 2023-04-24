n = int(input())
for _ in range(n):
    x = str(input().strip())
    ans = 0
    for i in x:

        if i == "(":
            ans += 1
        else:
            ans -= 1
        if ans < 0 :
            print("NO")
            break
    if ans == 0:
        print("YES")
    elif ans > 0:
        print("NO")
