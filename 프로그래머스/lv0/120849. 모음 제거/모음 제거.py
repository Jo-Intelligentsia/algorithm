def solution(my_string):
    answer = ''
    str_ = 'aeiou'
    for i in range(len(my_string)):
        if my_string[i] not in str_:
            answer += my_string[i]
    return answer