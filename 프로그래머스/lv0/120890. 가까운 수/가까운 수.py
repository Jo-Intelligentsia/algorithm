def solution(array, n):
    # answer = abs(array[0]-n)

    # for i in array:
    #     if abs(i-n) < answer:
    #         result = i
    #     elif abs(i-n) == answer:
    #         if i > result :
    #             pass
    #         elif i < result:
    #             result = i   
    # return result
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