def solution(clothes):
    #딕셔너리 생성
    obj = {}
    # 스파이가 갖고있는 의상의 수는 최소 1개 이상
    ans = 1
    
    # clothes 배열을 돌면서 키와 벨류를 뽑아 딕셔너리에 append
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in obj:
            obj[key].append(value)
        else:
            obj[key] = [value]
    # print(obj)
    # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}

    for key in obj:
        # 안입는 경우 +1 
        ans = ans * (len(obj[key]) + 1)
        # 모두 안입는 경우도 포함되었으니 -1
    return ans -1 