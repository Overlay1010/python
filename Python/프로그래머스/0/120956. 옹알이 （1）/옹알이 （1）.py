def solution(babbling):
    answer = 0
    a = ['aya','ye','woo','ma']
    for i in babbling:
        for j in a:
            i = i.replace(j," ",1)
        if len(i.strip())==0:
            answer+=1
    return answer
