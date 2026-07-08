def solution(x, n):
    answer = []
    a = x
    while n:
        answer.append(x)
        x+=a
        n-=1
    return answer