def solution(cipher, code):
    answer = ''
    i = 1
    while True:
        answer+= cipher[(code*i)-1]
        i+=1
        if (code*i)-1 >= len(cipher):
            break
        
    return answer