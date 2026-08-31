def solution(num_list):
    answer = 1
    a = sum(num_list)**2
    b = 1
    for i in num_list:
        b*=i
    if a < b:
        answer =0
        
    return answer