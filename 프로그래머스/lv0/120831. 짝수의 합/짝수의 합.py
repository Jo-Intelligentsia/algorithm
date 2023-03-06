def solution(n):
    answer = 0
    if n//2 == 0:
        for i in range(1,n//2+1):
            answer += 2*i
    else:
        for i in range(1,n//2+1):
            answer += 2*i
            
                
        
    # if n//2 == 0: # 짝수
    #     while True:
    #         answer += n
    #         n = n - 2
    #         if n == 0:
    #             break
    # else:
    #     n = n-1
    #     while True:
    #         answer += n
    #         n = n - 2
    #         if n == 0:
    #             break
    return answer