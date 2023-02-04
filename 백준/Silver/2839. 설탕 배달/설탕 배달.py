N = int(input()) # 설탕무게

bag = 0
while True:
    if N%5 == 0:
        break
    N -=3
    bag +=1
    if N <3:
        if N == 0:
            break
        bag = -1
        # print(-1)
        break
if bag == -1 :
    print(-1)
else:
    print(bag + N//5)