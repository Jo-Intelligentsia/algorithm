def solution(my_string):
    answer = ''
    low = my_string.lower()
    print(low)
    a = sorted(low)
    for i in a:
        answer+=i
    return answer