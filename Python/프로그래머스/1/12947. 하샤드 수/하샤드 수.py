def solution(x):
    answer = True
    x = str(x)
    st = ""
    n = 0
    for i in x:
        n+= int(i)
        st +=i
    if int(st) % n !=0:
        answer =False
    return answer