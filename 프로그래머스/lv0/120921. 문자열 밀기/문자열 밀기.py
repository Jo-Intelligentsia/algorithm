def solution(A, B):
    answer = 0
    if A == B :
        answer = 0
    elif sorted(A) != sorted(B):
        answer = -1
        print(sorted(A))
    else:
        while True:
            if A == B:
                break
            elif answer == len(A):
                answer = -1
                break
            answer += 1
            b = A[-1]
            A = A[-1] + A[:len(A)-1]
    return answer