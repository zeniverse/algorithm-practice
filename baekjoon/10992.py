# n = int(input())

# print(' ' * (n - 1) + '*')
# for i in range(2, n):
#     print(' ' * (n - i) + '*' + ' ' * (i * 2 -3) + '*')

# print('*' * (2 * n - 1))

n = int(input())

for i in range(1, n + 1):
    if i == 1 or n == i:
        print(' ' * (n - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')