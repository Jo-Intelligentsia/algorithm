def solution(numbers, k):
    answer = 0
    m = 0
    cnt = 1
    while cnt !=k:
        cnt +=1
        m += 2
        if m == len(numbers) + 1:
            m = 1
        elif m == len(numbers):
            m = 0
    return numbers[m]

