def solution(n):
    answer = [[0]* n for _ in range(n)]
    i = 0
    for i in range(n):
        answer[i][i]+=1
        
    return answer
        