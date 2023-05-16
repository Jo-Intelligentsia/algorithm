def solution(a, b, n):
    answer = 0
    while (n >= a): # 총 콜라가 빈병교환 개수보다 작거나 같을 때 반복 종료
        bottle = n % a # 빈병 교체 할수 있는 수량을 제외한 수
        n = (n//a) * b # 새로 받는 콜라의 수
        answer += n 
        n += bottle # 남아있는 콜라와 새로 받은 콜라를 합친수
    return answer