n, k = map(int, input().split())

tbl = [i for i in range (1, n + 1)]
pt = 0
ans = []
for _ in range(n):
    pt += k - 1
    pt %= len(tbl)
    ans.append(tbl.pop(pt))
print(f"<{', '.join(map(str, ans))}>")