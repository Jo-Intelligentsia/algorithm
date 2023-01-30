T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
# H,W,N = 30, 50, 72
# H : 층수 W : 호수 N : 손님수
# print(H,W,N)
    num = N//H+1 # 호수
# print(num)
    num1 = N%H # 층수
# print(num1)
    if num1 ==0:
        num1 = H
        num = N//H
        num_ = (num1 *100)+num
    else:
        num_ = (num1 *100)+num
    print(num_)