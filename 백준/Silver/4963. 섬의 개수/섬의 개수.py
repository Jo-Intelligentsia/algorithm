import sys

SEA = 0 # 바다
LAND = 1 # 섬
VISITED = 2 # 인접한 섬 1->2 로 변경


# solution
def find_land(lst2d_, stack):  # 델타 로 인접 확인 함수
    height = len(lst2d_)  # 높이는 입력값의 개수
    width = len(lst2d_[0]) # 너비는 입력값 첫번째 리스트 내의 개수
    delta = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]   # 인접한 리스트를 찾기위한 리스트
    
    while stack:
        x, y = stack.pop() # 스택에 삽입된 리스트 대입
        for dx, dy in delta: # 델타 값 반복
            x2 = x + dx # 델타값 위치 의 좌표 확인 
            y2 = y + dy # 델타값 위치 의 좌표 확인
            if (x2 < 0) or (x2 >= height) or (y2 < 0) or (y2 >= width):
                # Finding out of area
                continue    # Skip  # 맵을 넘어가면 패스
            
            if lst2d_[x2][y2] == LAND: # 
                stack.append((x2, y2))
                lst2d_[x2][y2] = VISITED  # Check visited land
                

def get_land_num(lst2d_): # 맵 입력값 받은 후
    ans = 0
    height = len(lst2d_) # 높이는 입력값의 개수
    width = len(lst2d_[0]) # 너비는 입력값 첫번째 리스트내의 개수
    
    for i in range(height): # i = 높이의 개수 만큼 반복
        for j in range(width): # j = 너비의 개수 만큼 반복
            stack = [] 
            if lst2d_[i][j] == LAND:   # Land not visited  # 입력값 차례대로 1,0 확인
                stack.append((i, j)) # 1이면 스택에 삽입
                lst2d_[i][j] = VISITED    # Check visited land #
                find_land(lst2d_, stack) # 삽입한 섬을 2로 변경후 인접한 섬이 있는지 확인하는 함수 적용
                ans += 1 # 섬의 갯수 추가
            
    return ans # 섬의 갯수 반환


# input & print
while True:
    width_num, height_num = map(int, sys.stdin.readline().split()) # 너비와 높이 입력값 받기
    if width_num == height_num == 0:    # End condition
        break
    
    # Input map shape
    map_shape_lst = []
    for _ in range(height_num): # 맵 입력값 받기
        map_shape_lst.append(list(map(int, sys.stdin.readline().split())))
    

    print(get_land_num(map_shape_lst))