from itertools import permutations

def solution(k, dungeons):
    ans = 0

    # 모든 던전 순열에 대해 탐색
    for dungeon_perm in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0

        # 순열의 각 던전을 방문하며 체력을 소모함
        for dungeon in dungeon_perm:
            if hp >= dungeon[0]:
                hp -= dungeon[1]
                count += 1
            else:
                break

        # 최대 클리어한 던전 수를 저장함
        ans = max(ans, count)

    return ans