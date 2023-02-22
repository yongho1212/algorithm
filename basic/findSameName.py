def findSameName(a):
    n = len(a)
    result = set()
    for i in range (0, n - 1):
        for j in range ( i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ['a', 'b', 'c', 'c', 'a']
print(findSameName(name))

# 배열에서 두명씩 짝을 지어 만들 수 있는 모든 조합을 출력하아
def liked(a):
    l = len(a)
    asn = []
    for i in range(0, l-1):
        for j in range(i+1, l):
            asn.append(a[i]+'-'+a[j])
    return asn

name = ['tom', 'jerry', 'pizza']
print(liked(name))