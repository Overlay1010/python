def solution(myString, pat):
    answer = 0
    s = []
    for i in myString:
        if i == 'A':
            i = 'B'
            s.append(i)
        else:
            i = 'A'
            s.append(i)
    if pat in "".join(s):
        answer = 1
    
    return answer