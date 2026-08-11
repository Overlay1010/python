def solution(myStr):
    answer = []
    current = ""
    a = ['a','b','c']
    for ch in myStr:
        if ch in a:
            if current !="":
                answer.append(current)
            current = ""
        else:
            current+=ch
    if current != "":
        answer.append(current)
        
    return answer if answer else["EMPTY"]