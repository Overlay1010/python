def solution(dots):
    answer = 0
    v = [(0,1,2,3),(0,2,3,1),(0,3,1,2)]
    for i,j,k,l in v:
        x1,y1 = dots[i]
        x2,y2 = dots[j]
        x3,y3 = dots[k]
        x4,y4 = dots[l]
        
        vx1 = x2-x1
        vy1 = y2-y1
        vx2 = x4-x3
        vy2 = y4-y3
        if (vx1 * vy2) - (vx2 * vy1) == 0:
            answer = 1

    return answer