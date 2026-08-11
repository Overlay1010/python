def solution(n):
    answer = []
    a= set()
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            a.add(d)
            n //= d
        d += 1
    if n > 1:
        a.add(n)
    answer = list(a)
    answer.sort()
    return answer