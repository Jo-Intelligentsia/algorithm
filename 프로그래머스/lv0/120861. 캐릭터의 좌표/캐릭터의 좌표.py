def solution(keyinput, board):
    result = [0,0]
    for i in keyinput:
        if i == 'up':
            if result[1] == (board[1]-1)//2:
                pass
            else:
                result[1] +=1
        elif i == 'down':
            if result[1] == -(board[1]-1)//2:
                pass
            else:
                result[1] -=1
        elif i == 'left':
            if result[0] == -(board[0]-1)//2:
                pass
            else:
                result[0] -=1
        elif i == 'right':
            if result[0] == (board[0]-1)//2:
                pass
            else:   
                result[0] +=1
    return result