com = int(input()) # 컴퓨터 개수
line = int(input()) # 라인 개수
graph = [[] for _ in range(com + 1)] # 컴퓨터 개수 만큼 반복
visited = [False] *(com +1)  # 컴퓨터 개수 만큼 생성
total = 0
# 인접 리스트 만들기
for _ in range(line):
    v1 , v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):  # 함수 생성 
    stack = [start] # 스택에 삽입
    visited[start] = True # 스타트 인덱스 True 변경
    total = 0
    while stack: # 스택이 0 이 되면 멈춤
        cur = stack.pop()
        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                total +=1
                stack.append(adj)
    return print(total)
dfs(1)