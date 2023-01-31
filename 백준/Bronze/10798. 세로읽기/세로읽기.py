matrix = [[0] * 15 for i in range(5)] # 5 * 15 이차원리스트 생성
for i in range(5): # 5줄 입력 받고
    string = list(input()) # 15개 이하의 문자열을 입력 받음
    string_len = len(string) 
    for j in range(string_len): # 입력값의 개수 만큼 반복
        matrix[i][j]=string[j] # 리스트에 입력값 대입
for i in range(15): # 열 우선 순회
    for j in range(5):
        if matrix[j][i] == 0:
            continue
        else:
            print(matrix[j][i],end='')