def solution(array, n):
 
    result = array[0]    # 가까운 값
    for i in array:
        # print(abs(i-n))
        if abs(i-n) < abs(result-n):
            result = i
        elif abs(i-n) == abs(result-n):
            if i < result:
                result = i
            else:
                pass
    return result