def solution(n):
    answer = 1
    i = 1
    while True:
        if answer <= n:
            answer = answer * (i + 1)
            i += 1
        else:
            i -= 1
            break
        
    return i