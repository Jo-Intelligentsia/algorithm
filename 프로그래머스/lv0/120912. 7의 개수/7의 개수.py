# def solution(array):
#     answer = 0
#     for i in array:
#         for j in str(i):
#             if '7' in str(j):
#                 answer += 1
#     return answer


def solution(array):
    answer = 0
    return str(array).count('7')