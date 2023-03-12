def solution(s):
    answer = 0
    m =[]
    s = s.split()
    for i in s:
        if i != 'Z':
            m.append(i)
        else:
            m.pop()
    for _ in range(len(m)):
        answer += int(m[_])
    return answer