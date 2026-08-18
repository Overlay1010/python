def solution(keyinput, board):
    x,y = 0, 0
    max_x, max_y = board[0] // 2, board[1] // 2
    for i in keyinput:
        if i == 'left' and x-1 >= -max_x:
            x-=1
        elif i == 'right' and x+1 <= max_x:
            x+=1
        elif i == 'down' and y-1 >= -max_y :
            y-=1
        elif i == 'up' and y+1 <= max_y :
            y+=1
    return [x,y]