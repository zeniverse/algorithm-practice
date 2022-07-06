board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

length = len(board)
popList = []
res = 0

for y in moves:
    for x in range(length):
        if board[x][y - 1] != 0:
            popList.append(board[x][y - 1])
            board[x][y - 1] = 0

            if len(popList) > 1:
                if popList[-1] == popList[-2]:
                    popList.pop()
                    popList.pop()
                    res += 2

            break

print(res)
