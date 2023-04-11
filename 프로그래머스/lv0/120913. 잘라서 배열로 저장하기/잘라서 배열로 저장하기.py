def solution(my_str, n):
    answer = []
    while True:
        # 문자열 개수가 n 보다 작아지면 남은 문자열 삽입 후 while 종료
        if len(my_str) <= n:
            answer.append(my_str)
            break
        else:
            # n 개의 문자열 삽입 후 n개를 제외한 나머지 문자열로 변환
            answer.append(my_str[:n])
            my_str = my_str[n:]
    return answer
