def solution(a, b):
    answer = 0
    pl = str(a)+str(b)
    total = 2*a*b
    if int(pl) > total:
        answer = int(pl)
    elif int(pl) < total:
        answer = total
    else:
        answer = int(pl)
    return answer