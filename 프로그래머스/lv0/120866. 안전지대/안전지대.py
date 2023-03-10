def solution(board):
    answer = 0
    dx = [-1,0,1]
    dy = [-1,0,1]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for k in dx:
                    for l in dy:
                        if 0 > i+k or i+k >= len(board) or 0 > j+l or j+l >= len(board):
                            pass
                        elif board[i+k][j+l] == 1 or board[i+k][j+l] == 2:
                            pass
                        else:
                            board[i+k][j+l] = 2

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer += 1
    return answer