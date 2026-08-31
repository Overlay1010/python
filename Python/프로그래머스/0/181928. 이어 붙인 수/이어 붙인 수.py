def solution(num_list):
    answer = 0
    a =''
    a2 = ''
    for i in num_list:
        if i % 2 !=0:
            a+=str(i)
        elif i % 2 ==0:
            a2+=str(i)
    answer = int(a)+int(a2)     
    return answer