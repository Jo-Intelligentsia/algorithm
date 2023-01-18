wood = list(input().split())
while True:
    for i in range(len(wood)):
            if i+1 == len(wood):
                break
            if wood[i] > wood[i+1]:
                wood[i],wood[i+1] = wood[i+1],wood[i]
                print(*wood)
    if wood == ['1','2','3','4','5']:
        break
        