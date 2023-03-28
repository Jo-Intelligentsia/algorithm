def solution(i, j, k):
    answer = 0
    ls = []
    for _ in range(i,j+1):
        for i in str(_):
            if k == int(i):
                answer +=1
            
    return answer