def solution(i, j, k):
    cnt = 0
    a = []
    for n in range(i,j+1):
        a.append(str(n))
    a = str(a)
    answer = a.count(str(k))
                       
    return answer