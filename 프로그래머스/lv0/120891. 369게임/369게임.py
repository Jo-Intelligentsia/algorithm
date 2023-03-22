def solution(order):
    answer = 0
    for i in str(order):
        # print(i)
        if str(i) in '369':
            answer += 1
    return answer