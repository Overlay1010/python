def solution(a, d, included):
    answer = 0
    lst = []
    n = len(included)
    lst.append(a)
    for i in range(n):
        lst.append(lst[i]+d)
    for j in range(n):
        if included[j]==True:
            answer+= lst[j]
        
    return answer