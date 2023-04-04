def solution(M, N):
    answer = 0
    answer += M-1 # 가로 절단값 추가
    answer += M * (N-1)
    return answer