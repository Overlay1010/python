def solution(my_str, n):
    answer = []
    a = 0
    while a < len(my_str):
        answer.append(my_str[a:a+n])
        a+=n
        
    return answer