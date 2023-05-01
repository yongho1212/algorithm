n = int(input())
st = sorted(list(map(int, input().split())))
m = int(input())
cp = list(map(int, input().split()))

def binary(t, arr, start, end):

    if start>end:
        return 0
    m = (start+end)//2
    if t == arr[m]:
        return 1
    elif t < arr[m]:
        return binary(t,arr,start, m-1)
    else:
        return binary(t,arr,m+1,end)

for i in cp:
    start = 0
    end = len(st) - 1 
    print(binary(i,st,start,end), end=" ")