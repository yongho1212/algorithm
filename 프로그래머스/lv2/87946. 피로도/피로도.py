from itertools import permutations
def solution(k, dungeons):
	# 던전의 번호: 0, 1, 2
    idx = [i for i in range(len(dungeons))]
    # 던전의 개수
    cnt = len(dungeons)
    
    # 최대 던전의 수에서 1씩 줄여간다: 3,2,1
    for i in range(cnt,0,-1):
    	# i개일 때의 던전의 순열을 구한다.
        for order in permutations(idx,i):
            now = k
            check = True
            for o in order:
                if dungeons[o][0] > now:
                    check = False
                    break
                else: 
                    now -= dungeons[o][1]
            if check:
                return i