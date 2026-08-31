def solution(num_list):
    answer = 0
    total = 0
    total2 = 0
    for i in range(len(num_list)):
        if i % 2 != 0:
            total += num_list[i]
        else:
            total2 += num_list[i]
    if total > total2:
        answer = total
    elif total < total2:
        answer = total2
    else:
        answer = total
    return answer