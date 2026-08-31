def solution(s):
    answer = True
    a = []
    b = []
    s.upper()
    for ch in s:
        if ch =='P' or ch =='p':
            a.append(ch)
        elif ch =='y' or ch =='Y':
            b.append(ch)
    if len(a)==len(b):
        answer = True
    else:
        answer = False        
    return answer
