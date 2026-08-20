def solution(dots):
    a = []
    b = []
    for i in range(4):
        a.append(dots[i][0])
        b.append(dots[i][1])
    a_n = max(a)- min(a)
    b_n = max(b)- min(b)
    
    return a_n*b_n
    