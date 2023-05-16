def solution(X, Y):
    answer = ''
    # 9부터 0까지 순회
    for i in range(9,-1,-1) :
        # i 가 x,y 에 있으면 
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
        
    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer