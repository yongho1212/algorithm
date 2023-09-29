def solution(s):
    s = s[2:-2]
    s = [x.split(',') for x in s.split('},{')]
    dic = {}

    for subset in s:
        for num in subset:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

    return [int(x) for x, _ in sorted(dic.items(), key=lambda x: -x[1])]
