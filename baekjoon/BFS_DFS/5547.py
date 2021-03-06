from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False]*m for i in range(n)]

# 연결된 0인 칸 탐색 후 테두리 개수 반환
def dfs(y, x):
    stack = [(y, x)]
    visited[y][x] = True
    cnt = 0
    while stack:
        y, x = stack.pop()
        if y%2 == 1 :
            diretions = [(-1,0), (-1,-1), (0,-1), (0,1), (1,0), (1,-1)]
        else:
            diretions = [(-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,1)]

        for i in diretions:
            ny = y + i[0]
            nx = x + i[1]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            
            if not visited[ny][nx]:
                if arr[ny][nx] : cnt+=1
                else :
                    visited[ny][nx] = 1
                    stack.append((ny, nx))
    return cnt


# 가장 바깥쪽 칸들과 연결된 칸 탐색
total = 0
for y in [0, n-1]: # 맨 위, 맨 아래 줄 탐색
    for x in range(m):
        if arr[y][x]:
            total += 2
            # 맨 위 오른쪽 or 맨 아래 왼쪽은 1m씩 추가되므로 1씩 빼준다 (추가 조건 3번)
            if (y==0 and x==m-1) or (y==n-1 and x==0):
                total -= 1

        elif arr[y][x]==0 and not visited[y][x]:
            # 바깥쪽 '0'칸이라면 dfs를 통해 탐색
            total += dfs(y, x)


for y in range(n): # 맨 오른쪽, 맨 왼쪽 줄 탐색
    for x in [0, m-1]:
        if arr[y][x] :
            # 오른쪽 홀수칸, 왼쪽 짝수칸은 3m씩 추가 (추가 조건 2번)
            if (x==0 and y%2 == 1) or (x==m-1 and y%2==0):
                total +=3
            else:
                # 왼쪽 홀수칸, 오른쪽 짝수칸은 1m씩 추가 (추가 조건 1번)
                total += 1

        elif arr[y][x]==0 and not visited[y][x]:
            total += dfs(y, x)

print(total)