def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1

        dfs(x-1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1

print(res)
