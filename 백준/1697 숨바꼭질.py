from collections import deque

n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX +1)
print(dist)
def bfs():
    q = deque() #큐 생성
    q.append(n) # 큐에 현위치 넣기
    while q: # q 가 참일동안
        x = q.popleft() # 큐에서 현위치 꺼내기
        if x == k : # 동생과 같은 위치이면
            print(dist[x]) # 결과 출력
            break # 종료
        for i in (x-1, x+1, x*2): # 선택할 수 있는 경우 3가지
            if 0 <= i <= MAX and not dist[i]: #이동한 위치가 0보다크고 max보다 작다 AND idx범위 밖이 아니다.
                dist[i] = dist[x] + 1 # 시간추가
                q.append(i) # 큐에 다음 위치 추가

bfs()