import itertools
import collections

def solution(orders, course):
    result = []
    for c in course:
        combinations = []
        for order in orders:
            combinations.extend(itertools.combinations(sorted(order), c))
        counter = collections.Counter(combinations)
        if len(counter) != 0 and max(counter.values()) != 1:
            result.extend([''.join(f) for f in counter if counter[f] == max(counter.values())])
    return sorted(result)
