def solution(n):
    answer = []
    a = 0
    # 1 ~ n 까지 반복
    while True:
        if n < a:
            break
        else:
            a +=1
            if n%a ==0:
                answer.append(a)
            
    return answer