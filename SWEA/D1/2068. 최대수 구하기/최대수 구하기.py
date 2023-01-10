T = int(input()) # 테스트 케이스 수
for t in range(1,T+1):
    num = list(map(int,input().split()))
    print(f'#{t} {max(num)}')