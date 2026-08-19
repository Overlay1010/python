def solution(rank, attendance):
    answer = 0
    a = []
    for i in range(len(attendance)):
        if attendance[i] == True:
            a.append(rank[i])
    a.sort()
    x = rank.index(a[0])
    y = rank.index(a[1])
    z = rank.index(a[2])
    answer = 10000 * x + 100 * y + z
    return answer