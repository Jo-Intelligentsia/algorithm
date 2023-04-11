def solution(A, B):
    answer = 0
    # 같으면 0 
    if A == B :
        answer = 0
    # 다른 문자가 있으면 -1
    elif sorted(A) != sorted(B):
        answer = -1
    else:
        while True:
            # A,B 같아지면 break
            if A == B:
                break
            # 총 횟수가 A 의 문자열 개수와 같아지면 옮겼을때 같을수가 없으므로
            elif answer == len(A):
                answer = -1
                break
            answer += 1
            b = A[-1]
            A = A[-1] + A[:len(A)-1]
    return answer