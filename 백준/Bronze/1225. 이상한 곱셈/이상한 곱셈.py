A,B = map(list,input().split()) # 숫자를 문자열로 입력 받음
A = list(map(int,A))
B = list(map(int,B))
print(sum(A)*sum(B))