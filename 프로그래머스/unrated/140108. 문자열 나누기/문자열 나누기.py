def solution(s):
    answer = 0 # 분해한 문자열의 개수
    while s:
        x = s[0] # 첫 글자를 x로 설정
        cnt_x, cnt_other = 0, 0 # x와 x가 아닌 다른 글자들의 횟수 초기화
        i = 0
        for i in range(len(s)):
            if s[i] == x: # 현재 글자가 x인 경우
                cnt_x += 1
            else: # 현재 글자가 x가 아닌 다른 글자인 경우
                cnt_other += 1
            if cnt_x == cnt_other: # x와 x가 아닌 다른 글자들의 횟수가 같아진 경우
                answer += 1 # 분해한 문자열 개수 증가
                s = s[i+1:] # 현재까지 분리한 문자열을 제외한 나머지 문자열로 업데이트
                break
        else: # for문을 끝까지 실행한 경우 (즉, 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없는 경우)
            answer += 1 # 분해한 문자열 개수 증가
            break # 종료
    return answer