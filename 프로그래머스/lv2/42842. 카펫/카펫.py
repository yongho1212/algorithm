
def solution(brown, yellow):
    # 총 카펫의 크기
    ssum = brown + yellow
    # 카펫의 크기가 될 수 있는 경우 탐색 
    # 노란색이 최소 1이므로 3부터 ~
    for i in range(3, ssum//2 + 1):
        # 카펫의 크기가 i로 나눠떨어지고 
        if ssum % i == 0 and i >= 2:
            # 세로 -2 * 가르 -2 가 노란색의 크기와 같은 경우
            if (i - 2) * (ssum//i - 2) == yellow:
                
                return [ssum//i, i]