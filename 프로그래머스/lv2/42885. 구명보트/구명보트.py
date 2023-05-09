def solution(people, limit):
    people.sort(reverse=True) # Sort in descending order
    
    cnt = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        # Check if the heaviest and lightest person can fit on the boat
        if people[i] + people[j] <= limit:
            cnt += 1
            i += 1
            j -= 1
        else:
            # Only the heaviest person can fit on the boat
            cnt += 1
            i += 1
    
    return cnt
