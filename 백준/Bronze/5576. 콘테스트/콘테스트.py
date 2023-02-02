w = []
k = []

for i in range(20):
    score = int(input())
    if i <= 9: # 10번째까지 입력값을 w 리스트에 저장
        w.append(score)
    else: # 11번째부터 입력값을 k 리스트에 저장
        k.append(score)
w.sort(reverse=True) # 내림차순으로 정렬
k.sort(reverse=True) # 내림차순으로 정렬
print(sum(w[:3]),sum(k[:3])) # 정렬된 리스트 중 앞의 3개를 합산해서 출력