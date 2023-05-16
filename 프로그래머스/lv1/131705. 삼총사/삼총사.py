def solution(number):
    answer = 0
    for i in range(len(number)-2): # 첫번째 자리 순회
        for j in range(i + 1, len(number)-1): # 두번째 자리 순회
            for k in range(j + 1, len(number)): # 세번째 자리 순회
                if number[i] + number[j] + number[k] == 0: # 총합이 0이면
                    answer += 1
    return answer