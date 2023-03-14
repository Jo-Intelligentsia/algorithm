def solution(array):
    answer = 0
    ls = []
    array.sort()
    while True:
        a = list(set(array))
        for i in a:         # 중복제거한 a 를 반복
            if i in array:  # 리스트에 있으면 제거
                array.remove(i) # 리스트에 중복된 값만 남음
                print(a,array)
        if len(a) == 1:
            return a[0]
            break
        elif len(array) == 0 and len(a) > 1:
            return -1
            break
