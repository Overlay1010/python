def solution(binomial):
    answer = 0 
    a = list(binomial.split())
    if a[1] == '+':
        answer = int(a[0]) + int(a[2])
    if a[1] == '-':
        answer = int(a[0]) - int(a[2])
    if a[1] == '*':
        answer = int(a[0]) * int(a[2])
    return answer