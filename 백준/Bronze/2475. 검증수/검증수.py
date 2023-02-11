n = list(map(int,input().split()))
result = 0
for i in n:
    result += i*i
print(result%10)