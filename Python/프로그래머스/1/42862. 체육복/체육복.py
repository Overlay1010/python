def solution(n, lost, reserve):
    reserve_n = [a for a in reserve if a not in lost]
    lost_n = [b for b in lost if b not in reserve]
    
    for i in sorted(reserve_n):
        if i - 1 in lost_n:
            lost_n.remove(i - 1)
        elif i + 1 in lost_n:
            lost_n.remove(i + 1)
    
    return n - len(lost_n)