def solution(n):
    answer = 0
    a = int(n**0.5)
    if n == a**2:
        return 1
    else:
        return 2
    # return answer