def solution(n):
    answer = 0
    m = n

    while True:
        if n % 6 == 0:
            return n//6
            break
        else:
            n +=m
    # return answer