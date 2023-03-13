def solution(my_string):
    answer = []
    num = '0123456789'
    for i in range(len(my_string)):
        if my_string[i] in num:
            answer.append(int(my_string[i]))
        
    answer.sort()
    return answer