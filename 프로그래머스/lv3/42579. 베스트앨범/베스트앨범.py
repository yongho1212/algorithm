# 장르별로 top2 
# 장르 총 합 순서대로


def solution(genres, plays):
    
    zipped = enumerate(zip(genres, plays))
    dict1={}
    dict2={}
    ans=[]
    
    for i,(g,p) in zipped:
        if g not in dict1:
            dict1[g] = [(i,p)]
        else:
            dict1[g].append((i,p))
        
        if g not in dict2:
            dict2[g] = p
        else:
            dict2[g] += p
    print(dict1)
    print(dict2)
            
    for (k, v) in sorted(dict2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dict1[k], key=lambda x:x[1], reverse=True)[:2]:
            ans.append(i)

    return ans