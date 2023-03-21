def solution(cipher, code):
    answer = ''
    # answer = cipher[code-1]
    for i in range(1,len(cipher)//code+1):
        answer += cipher[(code)*i-1]
    return answer