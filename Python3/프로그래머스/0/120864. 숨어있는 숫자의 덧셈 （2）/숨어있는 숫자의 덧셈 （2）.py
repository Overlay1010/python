def solution(my_string):
    answer = 0
    b = []
    a = ['1','2','3','4','5','6','7','8','9','0']
    for i in my_string:
        if i not in a:
            my_string = my_string.replace(i," ")
    my_string = list(my_string.split())
    for n in my_string:
        answer+=int(n)


    return answer