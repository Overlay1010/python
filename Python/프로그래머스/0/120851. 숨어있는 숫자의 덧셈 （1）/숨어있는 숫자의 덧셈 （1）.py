def solution(my_string):
    answer = 0
    for ch in my_string:
        if ch in "1234567890":
            answer +=int(ch)
    return answer