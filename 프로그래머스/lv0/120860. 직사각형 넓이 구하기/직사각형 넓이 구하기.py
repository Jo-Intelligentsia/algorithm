def solution(dots):
    answer = 0
    x = []
    y = []
    for i in range(len(dots)):
        x.append(dots[i][0])
        y.append(dots[i][1])

    answer = (max(x)-min(x)) * (max(y)-min(y))
    
    return answer