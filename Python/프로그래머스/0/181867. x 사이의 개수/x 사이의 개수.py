def solution(myString):
    answer = []
    a = 0
    for i in myString:
        if i != 'x':
            a+=1        
        elif i == 'x':
            answer.append(a)
            a=0
        else:
            answer.append(a)
    answer.append(a)
    
    return answer