def solution(balls, share):
    answer = 0
    a = 1
    b = 1
    c = 1
    n = balls
    m = share
    for i in range(1,n+1):
        a *= i
    for j in range(1,m+1):
        b *= j
    for k in range(1,n-m+1):
        c *= k
    answer = int(a/(c*b))
        
    return answer