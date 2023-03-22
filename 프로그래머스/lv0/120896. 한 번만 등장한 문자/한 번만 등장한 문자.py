def solution(s):
    answer = ''
    s = sorted(s)
    for i in s:
        if s.count(i) == 1:
            answer += i
    return answer