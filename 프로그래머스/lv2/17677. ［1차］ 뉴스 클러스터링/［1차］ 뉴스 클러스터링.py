from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    lst1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    lst2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    counter1 = Counter(lst1)
    counter2 = Counter(lst2)

    intersection = sum((counter1 & counter2).values())
    
    union = sum((counter1 | counter2).values())

    if union == 0:
        return 65536

    return int(intersection / union * 65536)
