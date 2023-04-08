def solution(array):
    answer = []
    a = max(array)
    answer.append(a)
    b= array.index(a)
    answer.append(b)
    return answer