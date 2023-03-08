def solution(spell, dic):
    answer = 0
    spell.sort()
    a = list(map(list,dic))
    for i in range(len(a)):
        a[i].sort()
        set(a[i])
        if a[i] == spell:
            answer = 1
            break
        else:
            answer = 2
    return answer