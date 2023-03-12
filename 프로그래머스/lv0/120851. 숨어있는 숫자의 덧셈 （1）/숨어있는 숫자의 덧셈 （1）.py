def solution(my_string):
    answer = 0
    num = '0123456789'
    for i in my_string:
        if i in num:
            answer += int(i)
    return answer