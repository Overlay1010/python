def solution(n, t):
    answer = n
    while t: 
        answer +=n
        n = n*2
        t-=1
    return answer