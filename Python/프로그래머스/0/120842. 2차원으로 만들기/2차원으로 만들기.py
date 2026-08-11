def solution(num_list, n):
    answer = []
    answer.append(num_list[:n])
    a = n
    while n < len(num_list):
        answer.append(num_list[n:n+a])
        n+=a
                          
    return answer