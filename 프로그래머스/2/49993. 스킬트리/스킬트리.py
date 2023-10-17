def solution(skill, skill_trees):
    ans = len(skill_trees)
    for tree in skill_trees:
        skill_list = list(skill)
        for s in tree:
            if s in skill_list:
                if s != skill_list.pop(0):
                    ans -= 1
                    break
    return ans
