def solution(num, k):
    answer = 0
    print(num)
    a = str(num).find(str(k))
    if a != -1:
        a +=1
    return a