from collections import deque

def solution(cacheSize, cities):
    cities = [item.lower() for item in cities]
    time = 0
    cache = deque([])
    
    if cacheSize == 0: return len(cities) * 5
    
    for city in cities:
        if len(cache) < cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                time += 1
            else :
                cache.append(city)
                time += 5
                
        if len(cache) >= cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                time += 1
            else :
                cache.popleft()
                cache.append(city)
                time += 5
    return time - 1