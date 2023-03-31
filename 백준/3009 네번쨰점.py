
arrx = []
arry = []

for _ in range(3):
    a,b = map(int, input().split())
    arrx.append(a)
    arry.append(b)

arrx.sort()
arry.sort()
x = ''
y = ''

if arrx.count(arrx[0]) > arrx.count(arrx[-1]):
    x = arrx[-1]
else:
    x = arrx[0]

if arry.count(arry[0]) > arry.count(arry[-1]):
    y = arry[-1]
else:
    y = arry[0]

print(x, y)