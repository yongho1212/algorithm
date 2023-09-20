from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_counter = Counter(dict(zip(want,number)))

    for i in range(len(discount) - 9):
        sublist = discount[i: i+10]
        sublist_counter = Counter(sublist)
        
        if want_counter == sublist_counter:
            answer += 1

    return answer
