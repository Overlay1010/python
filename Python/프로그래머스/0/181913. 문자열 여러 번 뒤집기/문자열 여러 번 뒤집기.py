def solution(my_string, queries):
    answer = ""
    lst = my_string
    for i in queries:
        a = lst[i[0]:i[1]+1]
        lst = lst[:i[0]] + a[::-1] + lst[i[1]+1:]
        # print(lst)
        answer = lst
        
    return answer