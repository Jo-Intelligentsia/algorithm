def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            print(j)
            if '7' in str(j):
                answer += 1
        print(i)
    return answer