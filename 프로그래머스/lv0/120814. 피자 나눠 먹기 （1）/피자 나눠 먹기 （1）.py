def solution(n):
    if n % 7==0:
        result = n//7
    else:
        result = n//7 + 1
    return result