def solution(id_pw, db):
    answer = ''
    id_pw[0] + id_pw[1]
    
    for i in db:
        if id_pw[0] == i[0] and i[1] == id_pw[1]:
            answer =  'login'
        elif id_pw[0] != i[0] and i[1] != id_pw[1]:
            answer = 'fail'
        elif id_pw[0] == i[0] and i[1] != id_pw[1]:
            answer = 'wrong pw'
    return answer