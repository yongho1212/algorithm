total = int(input())
itm = int(input())
Sum = 0

for i in range(itm):
    prdPrice, prdCnt = map(int, input().split())
    Sum = Sum + prdPrice * prdCnt
if Sum == total:
    print("yes")
else:
    print("No")