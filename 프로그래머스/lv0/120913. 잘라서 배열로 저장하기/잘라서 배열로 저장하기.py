def solution(my_str, n):
    answer = []
    while True:
        if len(my_str) <= n:
            answer.append(my_str)
            break
        else:
            answer.append(my_str[:n])
            my_str = my_str[n:]
    return answer
