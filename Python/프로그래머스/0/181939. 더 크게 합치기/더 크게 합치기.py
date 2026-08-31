def solution(a, b):
    answer = 0
    x = str(a)+str(b) 
    y = str(b)+str(a)
    if int(x) >= int(y):
        answer = int(x)
    else:
        answer = int(y)
    return answer