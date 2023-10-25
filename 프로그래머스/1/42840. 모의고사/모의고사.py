def solution(answers):
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] *1500
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if answers[i] == one[i]:
            cnt1 += 1
        if answers[i] == two[i]:
            cnt2 += 1
        if answers[i] == three[i]:
            cnt3 += 1
    scores = [cnt1, cnt2, cnt3]
    max_score = max(scores)

    return [i+1 for i, score in enumerate(scores) if score == max_score]
    