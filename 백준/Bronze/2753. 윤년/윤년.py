y = int(input())

if (0 == y %4) and (0 != y%100) or (0 == y%400):
    print('1')
else:
    print('0')

