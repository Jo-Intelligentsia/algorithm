def solution(my_string):
    answer = ''
    for i in my_string:
        if i == i.upper():
            answer += i.lower()
        elif i == i.lower():
            answer += i.upper()
    return answer