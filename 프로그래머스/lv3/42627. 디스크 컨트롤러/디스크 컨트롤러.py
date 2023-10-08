import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    current_time = jobs[0][0]
    while count < len(jobs):
        for s in jobs:
            if last < s[0] <= current_time:
                # 작업 소요시간으로 min heap을 만들기 위해 (소요시간, 시작시간) 튜플로 묶어서 저장한다.
                heapq.heappush(heap, (s[1], s[0]))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = current_time
            term_spend_time , start_time= heapq.heappop(heap)
            current_time += term_spend_time
            answer += (current_time - start_time)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            current_time += 1
    return int(answer / len(jobs))
