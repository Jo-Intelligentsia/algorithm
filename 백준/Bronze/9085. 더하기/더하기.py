T = int(input())
nums_sum = 0
for i in range(T):
    num = int(input())
    nums = map(int,input().split())
    nums_sum = sum(nums)
    print(nums_sum)