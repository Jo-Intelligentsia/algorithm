def solution(numbers):
    result = numbers[0]*numbers[1]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if result < numbers[i]*numbers[j]:
                result = numbers[i]*numbers[j]
    return result