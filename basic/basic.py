a = 5.
print(a)
a1 = 1e2
print(a1)
a2 = 0.3 + 0.6
print(a2)
print(round(a2,4))

c1 = 7
c2 = 3
print(c1/c2, c1%c2, c1//c2, c1**c2)

lst1 = [1,2,3,4,5,6,7,8,9]
print(lst1)
print(lst1[2])
print(lst1[2:4])

# 빈배열 선언하기
lst1 = []

# 크기가 n이고 모든 값이 0인 배열 만들기
# n = 0
# a = [0] * n

# 리스트 컴프리헨션 = 리스트 초기화, 2차원 배열 초기화에 효과적
arr1 = [i for i in range(20) if i % 2 == 0]
print(arr1)

arr2 = []
for j in range(20):
    if j % 2 == 1:
        arr2.append(j)
print(arr2)

arr3 = [i*i for i in range(1,10)]
print(arr3)

a = [1,2,6,4]
print(a)
a.append(3)
print(a)
# a.sort(reverse=True)
# print(a)
a.reverse()
print(a)
#2번 자리에 3추가
a.insert(2,3)
print(a)
# 특정 원소 수 새기
print(a.count(3))
# 특정 원소 한개 제거 - 인텍스가 낮은 값
a.remove(3)
print(a)

# 배열에서 특정 원소 모두 제거
a = [1,2,3,4,5,5,5]
remove_set = [3, 5]
result = [i for i in a if i not in remove_set]
print(result)

# 배열에서 중복 제거
res1 = set(a)
print(res1)
res2 = list(res1)
print(res2)

# 튜플 자료형
# 한번 선언된 값은 변경할 수 없다.
# 리스트는 대괄호를 쓰지만 [] 튜플은 소괄호를 쓴다 ()
a = (1, 2, 3, 4)
print(a[2])
# a[2] = 9

#사전 자료형
#key 와 value쌍으로 데이터를 가지는 자료형
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'
print(data)
if '사과' in data:
    print('사과있음')

kes = data.keys()
vals = data.values()
print(kes)
for key in kes:
    print(data[key])

# Set 집합자료형
# 중복을 허용하지 않는다. / 순서가 없다. / 특정데이터가 등장한 적이 있는지 확인할때 효과적이다.
data = set([1,1,1,2,3,3,4,4,4,5,5,])
print(data)

# 집합 자료형의 연산
a = set([1,2,3,4,5])
b = {3, 4, 5, 6, 7}
#합집합
print(a | b)
#교집합
print(a & b)
#차집합
print(a - b)

#원소 1개추가 add
a.add(6)
print(a)

# 원소 여러개 추가
a.update([7,8])
print(a)

# 특정 값을 갖는 원소 삭제
a.remove(3)
print(a)

print(1 in a)
# True
print(11 not in a)
# True

score = 85
if score >= 80:
    pass
    print('over 80')
else :
    print('under 80')

if score >= 80:result="success"
else: result="fail"

result= 'suc' if score >=80 else 'fail'

# 3항연산자 다시보기 -------------
result= score >= 80 and 'suc' or 'fail'
print(result,"3")

# 여기도 이해하고 넘어가기... 다시 보기
p = [1,2,3,4,5,5,5]
remove_set = {3,5}
print(p)
result = []
for i in p:
    if i not in remove_set:
        result.append(i)
print(result, '1')
result = [i for i in p if i not in remove_set]
print(result, "result")

j = 0
result = 0
while j < 9:
    result += i
    j += 1
print(result)
