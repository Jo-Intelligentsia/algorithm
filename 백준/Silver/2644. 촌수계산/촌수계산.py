def dfs(v):                         # dfs 함수 생성
    visited[v] = True               # A 부터 출발 
    for i in graph[v]:              # A 리스트 안에 있는 수를 반복
        if not visited[i]:          # 만약 A 리스트 안에 있는 수들이 없는 경우
            res[i] = res[v] + 1     # res i 번째를 res A 리스트 + 1로 변경
            dfs(i)

n=int(input())                      # n 전체 사람의 수 
A,B=map(int,input().split())        # A,B 촌수 계산 해야할 서로 다른 사람
m=int(input())                      # m 부모 자식들 간의 관계의 개수

graph=[[] for _ in range(n+1)]      # 방문을 기록할 리스트 생성
visited = [False] * (n + 1)         # 방문전 
res=[0]*(n+1)                       # 


for _ in range(m):                  # 관계 수 만큼 반복
    a,b=map(int,input().split())    # a,b 로 관계 입력 받기
    graph[a].append(b)              # a번째 리스트에 b 삽입
    graph[b].append(a)              # b번째 리스트에 a 삽입

dfs(A)                              # 첫번째로 촌수 계산을 시작할 사람을 함수에 대입

if res[B]>0:
    print(res[B])
else:
    print(-1)