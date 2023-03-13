def solution(numer1, denom1, numer2, denom2):
    answer = []
    num = numer2*denom1 + numer1*denom2 # 분자
    deno = denom1*denom2                # 분모

    gcd = 0
    # num과 deno의 최대공약수 구하기
    for j in range(min(num,deno), 0, -1):
        if num % j == 0 and deno % j ==0:
            gcd = j
            break
    
    answer = [num//gcd, deno//gcd]
    return answer