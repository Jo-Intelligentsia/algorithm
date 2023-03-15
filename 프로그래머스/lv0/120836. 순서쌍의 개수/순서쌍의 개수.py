def solution(n):
    answer = 0
    m = 1
    while True:
        if m > n:
            break
        if n%m == 0:
            answer += 1
        m +=1
    return answer