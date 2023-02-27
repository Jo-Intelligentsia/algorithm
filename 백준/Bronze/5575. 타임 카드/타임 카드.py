for _ in range(3):
    A = list(map(int,input().split()))
    # B = map(int,input().split())
    # C = map(int,input().split())

    a1 = A[0]*3600 + A[1]*60 + A[2]
    a2 = A[3]*3600 + A[4]*60 + A[5]

    A = a2-a1
    at_ = A//3600 # 시각
    am_ = (A%3600)//60
    as_ = (A%3600)%60%60
    print(at_,am_,as_)