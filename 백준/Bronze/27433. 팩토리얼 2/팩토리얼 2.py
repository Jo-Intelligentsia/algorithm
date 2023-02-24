def a(n):
    if n == 0:
        return 1
    else:
        return n * a(n-1)

b = int(input())
print(a(b))